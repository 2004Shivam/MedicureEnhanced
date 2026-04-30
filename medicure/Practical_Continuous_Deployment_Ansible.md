# Practical Record: Implementing Continuous Deployment using Ansible

**Objective:**
To implement and document a Continuous Deployment (CD) pipeline using Ansible for the containerized "Medicure" Django web application.

---

## 1. Prerequisites & Environment Status

Before creating the automated Ansible pipeline, we verified that the existing Medicure project (running on Django and PostgreSQL via Docker) was fully functional. The existing stack uses `docker-compose` to manage the web and db services.

**Command Executed:**
```bash
docker ps
```

**Output Screenshot:**
![Docker Status Selection](file:///home/shivam/Downloads/SEM1/MedicureEnhanced/medicure/screenshots/terminal_docker_ps.png)

**Application Running (Manual check):**
![Medicure App Initial State](file:///home/shivam/Downloads/SEM1/MedicureEnhanced/medicure/screenshots/medicure_homepage_deployed_1776436346893.png)


---

## 2. Ansible Installation & Workspace Setup

To maintain a clean environment without conflicting with system Python packages, Ansible was installed inside an isolated Python virtual environment.

**Commands Executed:**
```bash
# Create and activate virtual environment
python3 -m venv ansible-venv
source ansible-venv/bin/activate

# Install Ansible
pip install ansible
```

---

## 3. Creating the Ansible Project Structure

We created a dedicated `ansible/` directory within the project root to store all continuous deployment configuration files. 

### Step 3.1: Inventory Configuration (`inventory.ini`)
The inventory file defines the target machines. Since we are testing CD locally on the same host, we targeted `localhost`.

**File Content (`ansible/inventory.ini`):**
```ini
[webservers]
localhost ansible_connection=local ansible_python_interpreter="{{ ansible_playbook_python }}"
```

### Step 3.2: Ansible Config (`ansible.cfg`)
Configured defaults to use the correct inventory file and output format for readable logs.

**File Content (`ansible/ansible.cfg`):**
```ini
[defaults]
inventory = inventory.ini
host_key_checking = False
stdout_callback = yaml
```

### Step 3.3: Verifying Configuration
We ran a ping test using the `ping` module to verify Ansible could communicate with `localhost` using the defined inventory.

**Command Executed:**
```bash
../ansible-venv/bin/ansible all -i inventory.ini -m ping
```

**Output Screenshot:**
![Ansible Ping Test](file:///home/shivam/Downloads/SEM1/MedicureEnhanced/medicure/screenshots/terminal_ansible_ping.png)

---

## 4. Developing the Continuous Deployment Playbook

The core of this practical is the `deploy.yml` playbook. This playbook completely automates the pipeline from tearing down old instances to performing health checks on the newly deployed containers.

### Playbook Features Developed:
1. **Pre-flight Checks:** Verifies that the `.env` secret file exists and that Docker is installed before attempting deployment.
2. **Environment Teardown:** safely stops and removes the currently running application containers.
3. **Build Stage:** Builds fresh Docker images, ensuring that any new code changes are embedded into the container.
4. **Deployment Stage:** Uses `docker-compose up -d` to spin up the web and database containers.
5. **Health Verification Stage:** Runs an automated HTTP check mapped to port 8000, waiting until it receives a status 200 OK, verifying successful startup.


**File Content snippet (`ansible/deploy.yml`):**
```yaml
---
- name: Deploy Medicure Application
  hosts: webservers
  become: false
  gather_facts: yes
  vars:
    project_dir: "{{ playbook_dir }}/../"

  tasks:
    - name: Verify Docker is available
      command: docker --version
      register: docker_check

    - name: Tear down existing Docker containers
      command: docker compose down
      args:
        chdir: "{{ project_dir }}"

    - name: Build Docker images
      command: docker compose build
      args:
        chdir: "{{ project_dir }}"

    - name: Start Docker containers
      command: docker compose up -d
      args:
        chdir: "{{ project_dir }}"

    - name: Wait for web service to be fully responsive
      uri:
        url: "http://localhost:8000"
        status_code: 200
        return_content: yes
      register: health_check
      retries: 10
      delay: 5
      until: health_check.status == 200
```

---

## 5. Executing the Continuous Deployment Pipeline

With the CD playbook ready, it was executed to automate the full deployment lifecycle of the Medicure project.

**Command Executed:**
```bash
../ansible-venv/bin/ansible-playbook -i inventory.ini deploy.yml
```

The playbook successfully executed all 25 defined tasks automatically without any human intervention.

**Automated Deployment Output Screenshot:**
![Ansible Deploy Automation](file:///home/shivam/Downloads/SEM1/MedicureEnhanced/medicure/screenshots/terminal_ansible_deploy.png)

---

## 6. Post-Deployment Verification

After Ansible reported a successfully completed pipeline (0 failed tasks), we verified the GUI to confirm the new containerized application iteration was live and functional.

**App Verification Screenshot 1 (Homepage):**
![Medicure App verify](file:///home/shivam/Downloads/SEM1/MedicureEnhanced/medicure/screenshots/medicure_app_running_1776434444629.webp)

**App Verification Screenshot 2 (Prediction Module):**
![Medicure Disease Prediction](file:///home/shivam/Downloads/SEM1/MedicureEnhanced/medicure/screenshots/medicure_disease_prediction_page_1776434895102.png)

---

## 7. Conclusion & Results

We successfully implemented a Continuous Deployment (CD) pipeline using Ansible. 

**Key Takeaways:**
*   **Zero Downtime Preparation:** The system completely removed manual docker commands.
*   **Idempotency:** Re-running the `ansible-playbook` command handles upgrades securely over and over.
*   **Verification:** The Ansible `uri` module provided instant automated health verification that the webserver was up, avoiding the need for manual browser checks post-deploy.

The CD mechanism guarantees consistent deployments for the Medicure Healthcare platform.
