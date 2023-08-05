import os
import sys
import argparse
from loguru import logger
from tepe.core import get_task
from tepe.utils.general import find_config, find_weights


def train_parser(subparser):
    parser = subparser.add_parser('train', help='Train your model.',)
    parser.add_argument("-t", "--task-file", "--task-name", type=str, required=True,
                        help="plz input your task description file or task name")
    parser.add_argument("-f", "--output-dir", "--folder", type=str,
                        help="train result folder, contains config.py and weigths.pth")
    parser.add_argument("-r", "--data-root", type=str, help="dataset root directory")
    parser.add_argument("-b", "--batch-size", type=int, help="batch size")
    parser.add_argument("-d", "--device", nargs='+', type=int,
                        help="device for training")
    parser.add_argument("--resume", action="store_true",
                        help="resume training")
    parser.add_argument("--max-epoch", type=int,
                        help="total epochs")
    parser.add_argument("-c", "--resume-ckpt", type=str, help="resume checkpoint file")
    parser.add_argument("--fp16", dest="fp16", action="store_true",
                        help="Adopting mix precision training.")
    parser.add_argument("--cache", dest="cache", action="store_true",
                        help="Caching imgs to RAM for fast training.")
    parser.add_argument("opts", default=None, nargs=argparse.REMAINDER,
                        help="Modify config options using the command-line")

    return parser


def eval_parser(subparser):
    parser = subparser.add_parser('eval', help='Evaluate your model.',)
    parser.add_argument("-t", "--task-file", "--task-name", type=str,
                        help="plz input your task description file or task name")
    parser.add_argument("-w", "--weights", type=str,
                        help="trained weights for eval")
    parser.add_argument("-f", "--folder", type=str,
                        help="run result folder, contains config.py and weigths.pth")
    parser.add_argument("-b", "--batch-size", type=int, help="batch size")
    parser.add_argument("-d", "--device", nargs='+', type=int,
                        help="device for evaluate")
    parser.add_argument("--fp16", dest="fp16", action="store_true",
                        help="Adopting mix precision evaluate.")
    parser.add_argument("--cache",  dest="cache", action="store_true",
                        help="Caching imgs to RAM for fast evaluate.")
    parser.add_argument("opts", default=None, nargs=argparse.REMAINDER,
                        help="Modify config options using the command-line")

    return parser


def predict_parser(subparser):
    parser = subparser.add_parser('predict', help='Predict your model.',)
    parser.add_argument("-t", "--task-file", "--task-name", type=str,
                        help="plz input your task description file or task name")
    parser.add_argument("-w", "--weights", type=str,
                        help="trained weights for predict")
    parser.add_argument("-s", "--source", type=str,
                        help="source image, video, dir, or webcam")
    parser.add_argument("-f", "--folder", type=str,
                        help="run result folder, contains config.py and weigths.pth")
    parser.add_argument("-o", "--output-dir", type=str,
                        help="predictions save path")
    parser.add_argument("-d", "--device", nargs='+', type=int,
                        help="device for predict")
    parser.add_argument("-v", "--view-img", action="store_true",
                        help="view the prediction")
    parser.add_argument("--nosave", action="store_true",
                        help="no save the results")
    parser.add_argument("--fp16", dest="fp16", action="store_true",
                        help="Adopting mix precision evaluate.")
    parser.add_argument("opts", default=None, nargs=argparse.REMAINDER,
                        help="Modify config options using the command-line")

    return parser


def export_parser(subparser):
    parser = subparser.add_parser('export', help='Export your trained model.',)
    parser.add_argument("-t", "--task-file", "--task-name", type=str,
                        help="plz input your task description file or task name")
    parser.add_argument("-i", "-w", "--weights", type=str,
                        help="trained weights for export")
    parser.add_argument("-f", "--folder", type=str,
                        help="run result folder, contains config.py and weigths.pth")
    parser.add_argument("-o", "--out-file", "--export-name", "--out-path", type=str,
                        help="exported model file")
    parser.add_argument('--input-size', "--imgsz", '--img-size', type=int,
                        help='export image size (pixels)')
    parser.add_argument("--input-name", default="images", type=str,
                        help="input node name of onnx model")
    parser.add_argument("--output-name", default="output", type=str,
                        help="output node name of onnx model")
    parser.add_argument("--opset", default=11, type=int,
                        help="onnx opset version")
    parser.add_argument('--dynamic', action='store_true',
                        help='ONNX/TF: whether the input shape should be dynamic or not')
    parser.add_argument("-b", "--batch-size", type=int,
                        help="batch size")
    parser.add_argument("-d", "--device", nargs='+', type=int,
                        help="device for predict")
    parser.add_argument("--fp16", dest="fp16", action="store_true",
                        help="Adopting mix precision evaluate.")
    parser.add_argument("--no-onnxsim", action="store_true", help="use onnxsim or not")
    parser.add_argument('--include', nargs='+',
                        default=['onnx'],
                        help='available formats are (torchscript, onnx, saved_model, pb, tflite, tfjs, tensorrt)')
    parser.add_argument('--trt-version', nargs='+',
                        default=['7'],
                        help='available formats are (7, 8)')
    parser.add_argument("--export-nms", dest="export_nms", default=False, action="store_true",
                        help="Export onnx with nms symbol for Tensorrt/Onnxruntime convert.")
    parser.add_argument("-p", "--precision", default="fp16", choices=["fp32", "fp16", "int8"],
                        help="The precision mode to build in, either fp32/fp16/int8, default: 'fp16'")
    parser.add_argument("--workspace", dest="workspace", default=1, type=int,
                        help="The max memory workspace size to allow in Gb, default: 1")
    parser.add_argument("--calib-input", dest="calib_input", type=str,
                        help="The directory holding images to use for calibration")
    parser.add_argument("--calib-cache", dest="calib_cache",
                        default='./calibration.cache', type=str,
                        help="The file path for INT8 calibration cache to use, default: ./calibration.cache")
    parser.add_argument("--calib-num-images", dest="calib_num_images", default=5000, type=int,
                        help="The maximum number of images to use for calibration, default: 1")
    parser.add_argument("--calib-batch-size", dest="calib_batch_size", default=1, type=int,
                        help="The batch size for the calibration process, default: 1")
    parser.add_argument("opts", default=None, nargs=argparse.REMAINDER,
                        help="Modify config options using the command-line")
    return parser


def make_parser():
    parser = argparse.ArgumentParser(description='TEPE')
    subparser = parser.add_subparsers()

    train_parser(subparser)
    eval_parser(subparser)
    predict_parser(subparser)
    export_parser(subparser)

    return parser.parse_args()


@logger.catch
def main():
    args = make_parser()

    command = sys.argv
    if len(command) == 1:
        os.system('tepe -h')
        exit()

    if command[1] == 'install':
        # TODO
        # pip install -r tepe/tasks/***/requirments.txt
        pass
    elif command[1] == 'service':
        # TODO
        pass
    else:
        # logger.info(args)
        if command[1] == 'train':
            task = get_task(args.task_file)
            task.merge(vars(args), exclude=['task_file', 'folder', 'opts'])
            task.train()

        if command[1] == 'eval':
            task_file = args.task_file if args.task_file is not None else \
                find_config(args.folder) if args.folder is not None else None
            task = get_task(task_file)
            task.merge(vars(args), exclude=['task_file', 'folder', 'opts'])
            if not task.weights:
                output_dir = args.folder if args.folder is not None else task.output_dir
                task.weights = find_weights(output_dir)
            task.eval()

        if command[1] == 'predict':
            task_file = args.task_file if args.task_file is not None else \
                find_config(args.folder) if args.folder is not None else None
            task = get_task(task_file)
            task.merge(vars(args), exclude=['task_file', 'folder', 'source', 'view_img', 'nosave', 'opts'])
            if not task.weights:
                output_dir = args.folder if args.folder is not None else task.output_dir
                task.weights = find_weights(output_dir)
            task.predict(args.source, view_img=args.view_img, save_img=not args.nosave)

        if command[1] == 'export':
            task_file = args.task_file if args.task_file is not None else \
                find_config(args.folder) if args.folder is not None else None
            task = get_task(task_file)
            task.merge(vars(args), exclude=['task_file', 'folder', 'opts'])
            if not task.weights:
                output_dir = args.folder if args.folder is not None else task.output_dir
                task.weights = find_weights(output_dir)
            task.export()


if __name__ == '__main__':
    main()