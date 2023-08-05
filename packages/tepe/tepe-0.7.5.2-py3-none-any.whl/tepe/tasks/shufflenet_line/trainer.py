from tepe.core import Trainer


class LineTrainer(Trainer):
    def preprocess_batch(self, data):
        data['img'] = data['img'].to(self.device, non_blocking=True)
        data['target'] = data['target'].to(self.device, non_blocking=True)

        return data