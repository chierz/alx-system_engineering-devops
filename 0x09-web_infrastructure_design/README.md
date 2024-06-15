# 0x09. Web Infrastructure Design

## Introduction
This project involves designing and understanding various web infrastructures, focusing on key components such as DNS, web servers, load balancers, and monitoring systems. By completing this project, we have learned to design scalable, secure, and efficient web infrastructures.

## Concepts Covered
- **DNS:** The system that translates human-friendly domain names into IP addresses.
- **Monitoring:** Tools and practices for tracking the health and performance of web infrastructure.
- **Web Server:** Software that serves web content to users (e.g., Nginx).
- **Network Basics:** Fundamental concepts like IP addresses, ports, and protocols.
- **Load Balancer:** Distributes incoming traffic across multiple servers to ensure reliability and performance, hence ensuring that no server is overloaded
- **Server:** A computer or software that provides services to other computers or users in a network.

## Learning Objectives
- Draw and explain a diagram of a web stack.
- Explain the roles of each component in the web infrastructure.
- Understand and explain system redundancy.
- Know acronyms such as LAMP (Linux, Apache, MySQL, PHP), SPOF (Single Point of Failure), and QPS (Queries Per Second).

## Project Tasks and Achievements

### Task 0: Simple Web Stack
**Infrastructure Design:**
- **1 Server**
- **1 Web Server (Nginx)**
- **1 Application Server**
- **1 Database (MySQL)**
- **Domain Name:** `foobar.com` configured with a `www` record pointing to IP `8.8.8.8`

**Components Explanation:**
- **Server:** The machine hosting the entire infrastructure.
- **Web Server:** Manages HTTP requests from users.
- **Application Server:** Hosts the business logic and application code.
- **Database:** Stores user data and application state.
- **DNS Record:** Maps the domain name to the server’s IP address.

**Issues Identified:**
- **SPOF:** Single point of failure.
- **Downtime during maintenance.**
- **Limited scalability.**

#### File:
- `0-simple_web_stack`

### Task 1: Distributed Web Infrastructure
**Infrastructure Design:**
- **2 Servers**
- **1 Web Server (Nginx)**
- **1 Application Server**
- **1 Load Balancer (HAproxy)**
- **1 Database (MySQL)**

**Enhancements:**
- **Load Balancer:** Distributes traffic to prevent overload and increase redundancy.
- **Database Replication:** Set up for primary-replica to improve reliability.

**Components Explanation:**
- **Load Balancer:** Ensures traffic is evenly distributed and provides failover capability.
- **Primary-Replica Database:** Increases data availability and redundancy.

**Issues Identified:**
- **SPOF in load balancer.**
- **Security vulnerabilities without firewall and HTTPS.**
- **Lack of monitoring.**

#### File:
- `1-distributed_web_infrastructure`

### Task 2: Secured and Monitored Web Infrastructure
**Infrastructure Design:**
- **3 Firewalls**
- **1 SSL Certificate (HTTPS)**
- **3 Monitoring Clients**

**Enhancements:**
- **Firewalls:** Protect against unauthorized access.
- **HTTPS:** Encrypts data between the server and users.
- **Monitoring:** Tracks performance and health of the infrastructure.

**Components Explanation:**
- **Firewalls:** Filter incoming and outgoing traffic for security.
- **SSL Certificate:** Provides secure communication.
- **Monitoring Tools:** Collect data on server performance and user activity.

**Issues Identified:**
- **SSL termination at load balancer.**
- **Single MySQL server for writes.**
- **Uniform server components.**

#### File:
- `2-secured_and_monitored_web_infrastructure`

### Task 3: Scale Up
**Infrastructure Design:**
- **1 Additional Server**
- **Clustered Load Balancers (HAproxy)**
- **Dedicated Servers for Web, Application, and Database**

**Enhancements:**
- **Clustered Load Balancers:** Improve reliability and distribution.
- **Dedicated Servers:** Improve performance and scalability.

**Components Explanation:**
- **Clustered Load Balancers:** Provide high availability and redundancy.
- **Dedicated Servers:** Separate roles to optimize resource usage and performance.

#### File:
- `3-scale_up`

## Repository
- GitHub repository: [alx-system_engineering-devops](https://github.com/chierz/alx-system_engineering-devops)
- Directory: `0x09-web_infrastructure_design`

