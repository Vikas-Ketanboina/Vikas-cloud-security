# Linux Security Investigation

## Objective

Practise investigating a Linux EC2 instance by examining system identity, running processes, listening network ports, and SSH authentication logs.

## Environment

- Platform: Amazon EC2
- Operating system: Amazon Linux 2023
- Access method: SSH
- Tools: Linux command line, `ps`, `ss`, `uptime`, `who`, `last`, `journalctl`, and `grep`

## Investigation Steps

### 1. Identify the system

Commands:

```bash
whoami
hostname
hostname -I
uptime
```

Purpose:
- Identify the current user and hostname.
- Check the instance's private IP address.
- Review system uptime and load information.

### 2. Inspect running processes

```bash
ps aux
```

Purpose: Review running processes and identify anything that warrants further investigation.

### 3. Inspect listening network ports

```bash
sudo ss -tulnp
```

Purpose: Identify listening TCP/UDP ports and, where permissions allow, the associated processes.

### 4. Review SSH authentication logs

```bash
sudo journalctl -u sshd --since "24 hours ago"
```

Search for authentication-related events:

```bash
sudo journalctl -u sshd --since "24 hours ago" \
  | grep -Ei "failed|invalid|authentication failure"
```

Purpose: Look for failed or invalid SSH authentication events in the selected time window.

## Observations

- The instance was running Amazon Linux 2023.
- SSH was listening on TCP port 22.
- The reviewed SSH logs contained successful public-key authentication activity.
- The targeted search did not return matching failed or invalid SSH authentication events for the searched period.

## Security Interpretation

Successful public-key authentication can be consistent with authorized access, but it must be correlated with expected user activity and source information.

No matching failed or invalid SSH authentication events were identified by the targeted search. This does not prove that the system is free of compromise or that no other suspicious activity occurred.

## Limitations

- The investigation covered only the commands and logs examined.
- Log retention and the selected time window affect what evidence is available.
- A complete investigation would also consider IAM activity, Security Group rules, system processes, network flows, and other relevant telemetry.

## Lessons Learned

- Investigations should begin with a clear question.
- Commands and log searches provide evidence, not absolute proof of security.
- Findings must be interpreted in context and documented with limitations.

## Further Improvements

- Automate log summarisation with Python.
- Correlate host logs with AWS CloudTrail events.
- Add sanitized screenshots and a repeatable investigation checklist.
