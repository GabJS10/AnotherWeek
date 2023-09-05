# AnotherWeek

This project is a week and task management system developed in Python that allows you to organize your daily tasks into weeks. It provides an intuitive command line interface (CLI) to create, edit, and view your weeks and tasks.

### Outstanding Features:

- Create custom weeks with days of the week.
- Add, edit and delete tasks for each day.
- Export your week and task data to an Excel file.
- Validations to avoid invalid operations.
- Management of multiple weeks.

### How to use:

1. Clone this repository to your local machine.
2. Install the necessary dependencies (Click, Pandas, tabulate).
3. Run CLI commands to manage your weeks and tasks.
Command Example:

+ python main.py add_week --name NewWeek: Create a new week.
+ python main.py edit_todo_day --week Week1 --day Monday --task "Task 1": Add a task to the Monday of Week1.
+ python main.py see_week --name Week1: Shows the tasks of Week1.
+ python main.py to_excel_one --week Week1: Export Week1 data to an Excel file.
