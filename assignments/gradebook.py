from gradebookentry import GradebookEntry
from gradebookentry import GradebookEntryDropLowestProject
from gradebookentry import GradeBookEntryDropLowestMidterm

class Gradebook:
    def __init__(self):
        self._entries = {}
        self._scores = {}

    def add_entry(self, cwid, entry):
        self._entries[cwid] = entry

    def calculate_scores(self):
        for (cwid, entry) in self._entries.items():
            self._scores[cwid] = self._calc_average(entry)

    def print_scores(self):
        for (cwid, score) in self._scores.items():
            print(cwid, '{0:.4f}'.format(score))

    def _calc_average(self, entry):
        me_avg = self._calc_midterm_exam_average(entry)
        pr_avg = self._calc_project_average(entry)
        fe = entry.get_final_exam_score()
        return (0.4 * me_avg) + (0.4 * pr_avg) + (0.2 * fe)

    def _calc_midterm_exam_average(self, entry):
        return self._average_scores(entry.get_midterm_exam_scores())

    def _calc_project_average(self, entry):
        return self._average_scores(entry.get_project_scores())

    def _average_scores(self, scores):
        avg = 0.0
        for score in scores:
            avg += score
        avg /= len(scores)
        return avg



def main(argv):
    gb = Gradebook()

#    ge = GradebookEntry()
    ge = GradebookEntryDropLowestProject()
    ge.add_midterm_exam_score(90.0)
    ge.add_midterm_exam_score(82.5)
    ge.add_project_score(75.5)
    ge.add_project_score(85.25)
    ge.add_project_score(100.00)
    ge.add_project_score(90.75)
    ge.add_final_exam_score(60.25)
    gb.add_entry(1234, ge)

#    ge = GradebookEntry()
    ge = GradebookEntryDropLowestProject()
    ge.add_midterm_exam_score(70.0)
    ge.add_midterm_exam_score(52.0)
    ge.add_project_score(35.25)
    ge.add_project_score(45.75)
    ge.add_project_score(60.00)
    ge.add_project_score(50.25)
    ge.add_final_exam_score(40.5)
    gb.add_entry(5678, ge)

    gb.calculate_scores()
    gb.print_scores()


if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
