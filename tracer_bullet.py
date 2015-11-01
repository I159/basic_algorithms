import sys
import inspect

def trace(f):
    def shot(*args, **kwargs):
        current_file = inspect.getfile(f)
        lines = inspect.getsourcelines(f)

        line_no = lines[1] - 1
        all_lines = lines[0]
        all_lines_no = []
        count = 0
        while count < len(all_lines):
            line_no += 1
            all_lines_no.append(line_no)
            all_lines_no.append(0)
            count += 1


        def bullet(frame, event, arg):
            if event != 'line' and current_file == frame.f_code.co_filename:
                if frame.f_lineno in all_lines_no:
                    ex_ind = all_lines_no.index(frame.f_lineno)+1
                    all_lines_no[ex_ind] += 1
            return bullet

        sys.settrace(bullet)
        res = f(*args, **kwargs)

        count = line_idx = 0
        report = []
        while count < len(all_lines_no):
            report .append('{}  {}:{}'.format(all_lines_no[count+1],
                all_lines_no[count],
                all_lines[line_idx]))
            count += 2
            line_idx += 1

        report = ''.join(report)
        print report
        return res
    return shot
