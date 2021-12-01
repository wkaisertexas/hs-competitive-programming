import datetime, math
if __name__=="__main__":
    pass
    n_cases = int(input())
    for x in range(n_cases):
        line = input()
        n_files = int(line.split(" ")[0])
        n_gigs = float(line.split(" ")[1])
        
        files = {}
        for y in range(n_files):
            file_f = input()
            
            time = file_f.split("M")[0] + "M"
            time = datetime.datetime.strptime(time, "%d/%m/%Y %I:%M %p")
            
            today = datetime.datetime(2019, 5, 27, 0, 0, 0)
            days = (today - time).days + (today - time).seconds / (24 * 3600)
            
            days = math.ceil(2 * days) / 2

            size = file_f.split("M ")[1].split(" ")[0] # I need to learn REGEX so bad, but it still works 
            size = int(size)
            size /= 1000
            print(size, " ", days) 
            score = size * days
            files[score] = (file_f.split(" ")[4], size)

        n_megs = n_gigs * 1000

        to_deplete = n_megs / 4

        while to_deplete > 0:
            min_score = max(files.keys())

            to_deplete -= files[min_score][1]
            print(f"{files[min_score][0]} {min_score:.3f}")
            files.pop(min_score)
