class BioNeuron:
    def __init__(self, layer_id):
        self.layer = layer_id
    def signal(self, input_protein):
        return f"Signal_Transduced_by_{self.layer}"
