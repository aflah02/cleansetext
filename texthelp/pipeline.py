class Pipeline:
    def __init__(self, list_of_preprocessing_steps):
        self.preproc_steps = list_of_preprocessing_steps
    def process(self, text):
        for step in self.preproc_steps:
            text = step.process(text)
        return text
    def explain(self):
        for ind, step in enumerate(self.preproc_steps):
            print(f"Step {ind+1}: {step.explain()}")
        return "Enjoy!"