from datetime import datetime

c = datetime.now()
projects = {}
Team = {}
tasks = {}
user_data = {}


def manage_project():
    while True:
        print("1. Create Project\n2. Create Task\n3. Create User\n4. Assign Task to User\n5. View Assigned Tasks\n"
              "6. Delete Task\n7. Print Project Details\n8. Update Project Status\n9. Delete Project\n"
              "10. Update Task Status\n11. Display All Projects\n12. Exit")
        choice = int(input("Enter your choice (1-12): "))

        if choice == 1:
            project_id = int(input("Enter project ID: "))
            if project_id in projects:
                print(f"Project {project_id} is already assigned.")
                continue

            project_name = input("Enter project name: ")
            project_description = input("Enter project description: ")
            team_id = input("Enter the team_id: ")
            if team_id in Team:
                print(f"Team {team_id} is already assigned to a project.")
                continue

            projects[project_id] = {
                "name": project_name,
                "description": project_description,
                "team_id": team_id,
                "tasks": {},
                "users": {},
                "status": "Not Started",
                "creation_time": datetime.now(),  # Added creation_time for the project
                "update_time": None  # Initialize update_time to None
            }
            Team[team_id] = {
                "name": project_name
            }

        elif choice == 2:
            project_id = int(input("Enter project ID for the task: "))
            if project_id not in projects:
                print(f"Project {project_id} does not exist.")
                continue

            task_id = int(input("Enter task ID: "))
            task_name = input("Enter task name: ")
            task_description = input("Enter task description: ")

            tasks[task_id] = {
                "name": task_name,
                "description": task_description,
                "project_id": project_id,
                "assigned_user": None,
                "status": "Not Started"  # Default status
            }
            projects[project_id]["tasks"][task_id] = {"name": task_name, "assigned_user": None, "status": "Not Started"}

        elif choice == 4:
            project_id = int(input("Enter project ID for task assignment: "))
            if project_id not in projects:
                print(f"Project with ID {project_id} does not exist.")
                continue

            task_id = int(input("Enter task ID for assignment: "))
            if task_id not in projects[project_id]["tasks"]:
                print(f"Task with ID {task_id} does not exist in project {project_id}.")
                continue

            user_id = int(input("Enter user ID for task assignment: "))
            if user_id not in user_data:
                print(f"User with ID {user_id} does not exist.")
                continue

            projects[project_id]["tasks"][task_id]["assigned_user"] = user_id
            print(f"Task {task_id} assigned to user {user_id} in project {project_id}.at {c}")

        elif choice == 5:
            user_id = int(input("Enter user ID to view assigned tasks: "))
            print(f"Tasks assigned to user {user_id}:")

            for project_id, project_info in projects.items():
                project_tasks = project_info["tasks"]
                for task_id, task_info in project_tasks.items():
                    if task_info["assigned_user"] == user_id:
                        print(f"Project ID: {project_id}, Task ID: {task_id}, Task Name: {task_info['name']}")

        elif choice == 7:
            project_id = int(input("Enter project ID to view details: "))
            if project_id in projects:
                project_info = projects[project_id]
                print(f"Project ID: {project_id}")
                print(f"Name: {project_info['name']}")
                print(f"Description: {project_info['description']}")

                project_tasks = project_info["tasks"]
                if project_tasks:
                    print("Tasks:")
                    for task_id, task_info in project_tasks.items():
                        task_creation_time = task_info.get("creation_time", "N/A")
                        task_update_time = task_info.get("update_time", "N/A")
                        print(
                            f"  Task ID: {task_id}, Name: {task_info['name']}, Assigned User: {task_info['assigned_user']}, Status: {task_info['status']}")
                        print(f"    Creation Time: {task_creation_time}, Update Time: {task_update_time}")
                else:
                    print("No tasks for this project.")

                print(f"Project Status: {project_info['status']} at {c}")

            else:
                print(f"Project with ID {project_id} does not exist.")

        elif choice == 3:
            user_id = int(input("Enter user ID: "))
            username = input("Enter username: ")
            password = input("Enter password: ")
            role = input("Enter user role (manager/developer): ")

            user_data[user_id] = {
                "username": username,
                "password": password,
                "role": role,
                "projects": []
            }

        elif choice == 6:
            project_id = int(input("Enter project ID for task deletion: "))
            if project_id not in projects:
                print(f"Project with ID {project_id} does not exist.")
                return

            task_id = int(input("Enter task ID for deletion: "))
            if task_id not in projects[project_id]["tasks"]:
                print(f"Task with ID {task_id} does not exist in project {project_id} at {c}")
                return

            del projects[project_id]["tasks"][task_id]
            print(f"Task {task_id} deleted successfully from project {project_id}.")

        elif choice == 8:
            project_id = int(input("Enter project ID to update status: "))

            if project_id in projects:

                new_status = input("Enter new project status (Not Started/In Progress/Completed): ")

                if new_status in ["Not Started", "In Progress", "Completed"]:

                    projects[project_id]["status"] = new_status
                    projects[project_id]["update_time"] = datetime.now()  # Update project update_time

                    print(f"Project {project_id} status updated to {new_status} at {datetime.now()}")

                else:

                    print("Invalid status. Please enter 'Not Started', 'In Progress', or 'Completed'.")

            else:

                print(f"Project with ID {project_id} does not exist.")

        elif choice == 9:
            project_id = int(input("Enter project ID to delete: "))
            if project_id in projects:
                del projects[project_id]
                print(f"Project {project_id} deleted at {c}")
            else:
                print(f"Project with ID {project_id} does not exist.")

        elif choice == 10:
            update_task_status()

        elif choice == 11:
            display_all_projects()

        elif choice == 12:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 12.")


def display_all_projects():
    print("Project ID\tProject Name\tStatus\t\t\tCreation Time\t\t\tLast Update Time")
    for project_id, project_info in projects.items():
        project_name = project_info['name']
        project_status = project_info['status']
        creation_time = project_info.get("creation_time", "N/A")
        last_update_time = project_info.get("update_time", "N/A")

        print(f"{project_id}\t\t{project_name}\t{project_status}\t\t{creation_time}\t\t{last_update_time}")


def update_task_status():
    project_id = int(input("Enter project ID for task status update: "))
    if project_id not in projects:
        print(f"Project with ID {project_id} does not exist.")
        return

    task_id = int(input("Enter task ID for status update: "))
    if task_id not in projects[project_id]["tasks"]:
        print(f"Task with ID {task_id} does not exist in project {project_id}.")
        return

    new_status = input("Enter new task status (Not Started/In Progress/Completed): ")
    if new_status in ["Not Started", "In Progress", "Completed"]:
        old_status = projects[project_id]["tasks"][task_id]["status"]
        projects[project_id]["tasks"][task_id]["status"] = new_status

        # Update the task update time
        projects[project_id]["tasks"][task_id]["update_time"] = datetime.now()

        print(
            f"Task {task_id} status updated from {old_status} to {new_status} in project {project_id} at {datetime.now()}")

        # Check if two tasks are completed
        completed_tasks = sum(1 for task in projects[project_id]["tasks"].values() if task["status"] == "Completed")
        if completed_tasks == 2:
            print("Congratulations! One milestone is completed.")
    else:
        print("Invalid status. Please enter 'Not Started', 'In Progress', or 'Completed'.")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user_id, user_info in user_data.items():
        if user_info["username"] == username and user_info["password"] == password:
            return user_id
    return None


admin_role = {
    'admin1': {
        'username': 'pro1',
        'password': 'pro1@123'
    },
    'admin2': {
        'username': 'pro2',
        'password': 'pro2@123'
    },
    'admin3': {
        'username': 'pro3',
        'password': 'pro3@123'
    },
}

while True:
    role = input("Are you a user or admin? ").lower()
    if role == 'admin':
        username = input("Enter your username : ")
        password = input("Enter your password : ")
        if username == admin_role['admin1']['username']:
            if password == admin_role['admin1']['password']:
                print("You are logged in as admin")
                manage_project()

    elif role == 'user':
        user_id = login()

        if user_id is not None:
            print(f"You are logged in as user {user_id}")

            while True:
                print("1. View Assigned Project\n2. View Project Details\n3. Exit")
                user_choice = int(input("Enter your choice (1-3): "))

                if user_choice == 1:
                    team_id = input("Enter your team ID: ")
                    if team_id in Team:
                        
                        project_name = Team[team_id]["name"]
                        print(f"Team {team_id} is assigned to project {project_name} at {c}")
                    else:
                        print(f"Team {team_id} is not assigned to any project.")
                elif user_choice == 2:
                    project_id = int(input("Enter project ID to update status: "))
                    if project_id in projects:
                        new_status = input("Enter new project status (Not Started/In Progress/Completed): ")
                        if new_status in ["Not Started", "In Progress", "Completed"]:
                            projects[project_id]["status"] = new_status
                            projects[project_id]["update_time"] = datetime.now()  # Update project update_time
                            print(f"Project {project_id} status updated to {new_status} at {c}")
                        else:
                            print("Invalid status. Please enter 'Not Started', 'In Progress', or 'Completed'.")
                    else:
                        print(f"Project with ID {project_id} does not exist.")

                elif user_choice == 3:
                    exit()
                else:
                    print("Invalid choice. Please enter a number between 1 and 3.") 

        else:
            print("Invalid credentials. Please try again.")

    else:
        print("Invalid role. Please enter 'admin' or 'user'.")
