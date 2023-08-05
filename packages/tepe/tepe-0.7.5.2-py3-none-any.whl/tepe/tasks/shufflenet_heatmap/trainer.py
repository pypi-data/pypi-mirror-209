from tepe.core import Trainer


class KeypointTrainer(Trainer):
    def preprocess_batch(self, data):
        data['img'] = data['img'].to(self.device, non_blocking=True)
        data['target'] = data['target'].to(self.device, non_blocking=True)
        if 'paf_maps' in data:
            data['paf_maps'] = data['paf_maps'].to(self.device, non_blocking=True)
        return data