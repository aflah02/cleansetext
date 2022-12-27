class Pipeline:

    def __init__(self, list_of_preprocessing_steps, track_diffs=False):
        self.preproc_steps = list_of_preprocessing_steps
        self.track_diffs = track_diffs
        self.diffs = []

    def process(self, text):
        diff_for_curent_process_call = []
        for step in self.preproc_steps:
            text_out = step.process(text)
            if self.track_diffs:
                diff_for_curent_process_call.append([text, text_out])
            text = text_out
        if self.track_diffs:
            self.diffs.append(diff_for_curent_process_call)
        return text

    def explain(self, show_diffs=False):
        if show_diffs:
            if not self.track_diffs:
                raise Exception("You need to set track_diffs=True to use this feature!")

        for ind, diff_step in enumerate(zip(self.diffs[-1], self.preproc_steps)):
            diff, step = diff_step
            print(f"Step {ind+1}: {step.explain()}")
            print(f"Diff: {diff[0]} -> {diff[1]}")