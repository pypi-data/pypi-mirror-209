
from loguru import logger
import torch


def load_pretrain_ignore_name(net, pretrained_file):
    pre_train = pretrained_file
    if pre_train == '':
        logger.info('the pre_train is null, skip')
        return
    else:
        # logger.info('the pre_train is %s ' %pre_train)
        new_dict = {}
        pretrained_model = torch.load(pre_train, map_location=torch.device('cpu'))

        pre_keys = pretrained_model.keys()
        net_keys = net.state_dict().keys()
        # logger.info('net keys len:%d, pretrain keys len:%d ' %(len(net_keys), len(pre_keys)))
        if len(net_keys) != len(pre_keys):
            # logger.info \
            #     ('key lens not same, maybe the pytorch version for pretrain and net are difficent; use name load')
            for key_net in net_keys:
                strip_key_net = key_net.replace('module.', '')
                if strip_key_net not in pre_keys:
                    # logger.info('op: %s not exist in pretrain, ignore ' %(key_net))
                    new_dict[key_net] = net.state_dict()[key_net]
                    continue
                else:
                    net_shape = str(net.state_dict()[key_net].shape).replace('torch.Size', '')
                    pre_shape = str(pretrained_model[strip_key_net].shape).replace('torch.Size', '')
                    if net.state_dict()[key_net].shape != pretrained_model[strip_key_net].shape:
                        # logger.info('op: %s exist in pretrain but shape difficenet(%s:%s), ignore' %
                        #             (key_net, net_shape, pre_shape))
                        new_dict[key_net] = net.state_dict()[key_net]
                    else:
                        # logger.info(
                        #     'op: %s exist in pretrain and shape same(%s:%s), load' % (key_net, net_shape, pre_shape))
                        new_dict[key_net] = pretrained_model[strip_key_net]

        else:
            for key_pre, key_net in zip(pretrained_model.keys(), net.state_dict().keys()):
                if net.state_dict()[key_net].shape == pretrained_model[key_pre].shape:
                    new_dict[key_net] = pretrained_model[key_pre]
                    # logger.info('op: %s shape same, load weights' % (key_net))
                else:
                    new_dict[key_net] = net.state_dict()[key_net]
                    # logger.info('op: %s:%s shape diffient(%s:%s), ignore weights' %
                    #              (key_net, key_pre,
                    #               str(net.state_dict()[key_net].shape).replace('torch.Size', ''),
                    #               str(pretrained_model[key_pre].shape).replace('torch.Size', '')))

        net.load_state_dict(new_dict, strict=False)
        logger.info('!!load pretrained model success!!')


def check_only_train(op_name, only_train_list):
    if len(only_train_list) == 0:
        return True
    else:
        for only_train_name in only_train_list:
            if only_train_name in op_name:
                return True
        return False
