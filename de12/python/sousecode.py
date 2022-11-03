import calendar
import datetime

import PySimpleGUI as sg


sg.theme('LightBlue6')
today = datetime.date.today()

def create_layout(cal_date):
    weekday = ['SUN','MON', 'TUE', 'WE', 'THU', 'FRI', 'SAT']  
    cal = calendar.Calendar(firstweekday=6)
    days = cal.monthdatescalendar(cal_date.year, cal_date.month)
    layout = [[sg.Text(cal_date.year, font=(None, 13, 'bold'))],
              [sg.Push(), sg.Button('<<'), sg.Button('<'), sg.Text(cal_date.month, font=(None, 30)), sg.Button('>'), sg.Button('>>'), sg.Push()]]
    inner = []
    
    for week in weekday:
        inner.append(sg.Text(week, size=(4,1), text_color='white', background_color='gray', justification='center'))
    layout.append(inner.copy())

    def date_judgement(i, day):
        if day == today:
            return sg.Text(day.day, size=(4,1), justification='right', text_color='white', background_color='gray')
        elif i == 0 and day.month == cal_date.month:
            return sg.Text(day.day, size=(4,1), justification='right', text_color='red')
        elif i == 6 and day.month == cal_date.month:
            return sg.Text(day.day, size=(4,1), justification='right', text_color='blue')
        elif day.month == cal_date.month:
            return sg.Text(day.day, size=(4,1), justification='right')
        elif i == 0:
            return sg.Text(day.day, size=(4,1), justification='right', text_color='#ff9999')
        elif i == 6:
            return sg.Text(day.day, size=(4,1), justification='right', text_color='#9999ff')
        else:
            return sg.Text(day.day, size=(4,1), justification='right', text_color='#cccccc')

    for row in days:
        inner = []
        for i, day in enumerate(row):
            sg_text = date_judgement(i, day)
            inner.append(sg_text)
        layout.append(inner.copy())
    return layout

def main():
    cal_date = today
    layout = create_layout(cal_date)
    window = sg.Window('Simple Calendar', layout)

    while True:
        event, _ = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == '<':
            cal_date = datetime.date(cal_date.year, cal_date.month, 1) - datetime.timedelta(days=1)
        elif event == '>':
            cal_date = datetime.date(cal_date.year, cal_date.month, 28) + datetime.timedelta(days=4)
        elif event == '<<':
            cal_date = datetime.date(cal_date.year - 1, cal_date.month, 1)
        elif event == '>>':
            cal_date = datetime.date(cal_date.year + 1, cal_date.month, 1)
        window.close()
        window = sg.Window('Simple Calendar', create_layout(cal_date))
    window.close()

if __name__ == '__main__':
    main()

import datetime
import heapq as hq


# タスクの情報を保持するクラス
class Task:
    # 本来は引数要素の型チェックを行うが省略
    def __init__(self, name, datetime):
        self.name = name
        self.datetime = datetime
    
    def __lt__(self, other):
        if not isinstance(other, Task):
            return NotImplemented
        return self.datetime < other.datetime


tasks = []

# タスクの追加
hq.heappush(tasks, Task("タスクA", datetime.datetime(2021, 4, 1)))
hq.heappush(tasks, Task("タスクA", datetime.datetime(2021, 6, 1)))
hq.heappush(tasks, Task("タスクA", datetime.datetime(2021, 5, 1)))

# タスクが存在する間ループ
while tasks:
    # タスクを取り出したくない場合はtask[0]を参照すればよい
    # 実行時刻を超えたらタスクをキューから取り出して処理する
    if tasks[0] <= datetime.datetime.now():
        task = hq.heappop(tasks)
        # タスクに対する何らかの処理
    # スリープ処理等
