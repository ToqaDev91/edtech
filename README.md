# Edtech Entrollment Application

Backend Django application for students enrollment

## Requirements

- Docker: https://docs.docker.com/engine/installation/
- Docker-compose: https://docs.docker.com/compose/install/

## Developer's setup

1. install docker and docker compose on your local PC (docker machine is optional)
2. update environment variables if needed for local deployment --> `devops/env/local`
3. Run `make image` to build needed images 
4. Run `make up` to make those images up containers 
5. Use superuser configuration from `devops/env/local` to login for admin screen 
6. Navigate to `http://localhost:8000/admin` to control CRUD operations for DB
7. Navigate to `http://localhost:8000/api/docs/` to see the swagger file 
8. Navigate to `http://localhost:8000/api/explorer/` to do queries on postgres from UI
9. Navigate to `http://localhost:8025/` to access mails sent and check format
10. Navigate to `http://localhost:5555/` to see celery job running/scheduled 

## Debugging

Follow these steps to set up remote debugging for `edtech` running inside a Docker container.

> You will need Visual Studio Code.Install the latest version of Visual Studio Code on your local machine.

1. Open `edtech` project folder in Visual Studio Code.

2. In VSCode, install the Python extension if you haven't already. This extension provides language support for Python and includes debugging features.

3. Update the launch.json file in VSCode to add a new launch configuration for remote debugging:

   - Open the Command Palette in VSCode by pressing `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS).
   - Type "Python: Add Configuration" and select the "Python: Add Configuration" option from the dropdown menu.

   - Choose the "Attach to Remote" option to add a new launch configuration for remote debugging.

   - Modify the newly added configuration to set the port as `5679` and the host parameter as `0.0.0.0`.

4. Build the Docker image and start the container:

   - Open a terminal window and navigate to the root folder of the `edtech` project.

   - Run the following command to build the Docker image: `make up`. This will build the necessary Docker image and start the container.

   - Once the container is running, the back-end application should be accessible.

5. Run the Python: Remote Attach entry in the run and debug tab.

Now you should be able to set breakpoint in the code and have VSCode suspend the thread on each breakpoint.

## Migrations 

- if you want to make new migration file call : `make build-migrations`
- if you want to run migrations call : `make migrate`

    if you want to run it for specific module `make migrate module=<module name>`

## Translations 

if you add/edit/remove keys from message.po file and want to complie messages again : 

 `make compile-trans`

## Data Builder
