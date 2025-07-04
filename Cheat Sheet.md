This is a quick Linux Cheat sheet to troubleshoot problems in Linux servers

1. subprocess.run("uname -a", shell=True)                   # Kernel and architecture info
2. subprocess.run("uptime", shell=True)                     # System uptime and load
3. subprocess.run("free -h", shell=True)                    # Memory usage
4. subprocess.run("df -h", shell=True)                      # Disk usage
5. subprocess.run("du -sh /path/to/dir", shell=True)        # Directory size
6. subprocess.run("top -b -n 1", shell=True)                # One-time snapshot of running processes
7. subprocess.run("w", shell=True)                          # User sessions and activity
8. subprocess.run("env > /tmp/env.txt", shell=True)  # Environment variables
9. subprocess.run("who", shell=True)                        # Logged-in users
10. Trobleshooting server code below:
