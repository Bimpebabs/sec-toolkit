# sec-toolkit

A curated reference of open-source security tools organized by engagement phase. Built for practitioners who need the right tool for the job.

Covers reconnaissance, web application testing, network assessment, identity and access, exploitation, container security, AI security, cloud posture, supply chain, detection engineering, incident response, and reporting. Each entry includes a brief note on when to reach for it.

**Scope:** Tools used in authorized security work. Penetration tests, red team engagements, purple team exercises, security assessments, and incident response.

**Not included:** Commercial-only tools, tools with no public source, anything primarily malicious in intent. Dual-use tools are included with context.

---

## Quick start

| Phase | Tool | Purpose |
|---|---|---|
| Recon | Subfinder | Passive subdomain discovery |
| Recon | httpx | Validate live subdomains |
| Web | Burp Suite Community | Web proxy for manual testing |
| Web | Nuclei | Template-based vulnerability scanning |
| AD | BloodHound | AD attack path analysis |
| AD | NetExec | Network execution and post-exploitation |
| Container | Trivy | Container and IaC vulnerability scanning |
| AI | Garak | LLM vulnerability scanner |
| Supply chain | Syft + Grype | SBOM generation and scanning |
| Detection | Sigma | Detection-as-code format |

---

## Contents

- Reconnaissance & OSINT
- Web Application Security
- Network & Infrastructure
- Identity & Access
- Exploitation & Post-Exploitation
- Container & Kubernetes Security
- AI / LLM Security
- Cloud Security Posture
- Supply Chain Security
- Detection Engineering & DFIR
- Reporting & Collaboration
- Distributions & Cyber Ranges
- Archived but Useful

---

## Reconnaissance & OSINT

### Subdomain & DNS enumeration

| Tool | Purpose | When to use |
|---|---|---|
| Subfinder | Passive subdomain discovery from dozens of sources | First step on any engagement |
| Amass | In-depth attack surface mapping with graph output | When Subfinder alone is not enough |
| dnsx | Fast multi-purpose DNS toolkit | Resolve and validate large subdomain lists |
| httpx | HTTP prober for validating live hosts | Pair with Subfinder to confirm live subdomains |
| katana | Web crawler with headless-browser support | Better than gau for modern JS-heavy apps |
| gau | Fetch known URLs from AlienVault, Wayback Machine, Common Crawl | Quick historical URL discovery |
| waybackurls | Wayback Machine URL fetcher | Lightweight alternative to gau |

### Port scanning

| Tool | Purpose | When to use |
|---|---|---|
| Nmap | Standard network scanner | Deep service detection and NSE scripting |
| Masscan | Internet-scale TCP port scanner | Large ranges, then hand off to Nmap for service detection |
| Naabu | Fast, reliable port scanner written in Go | Middle ground between Masscan and Nmap |
| RustScan | Modern port scanner that pipes into Nmap | Fast for CTFs and quick assessments |

### Search engines & threat intel

| Tool | Purpose | When to use |
|---|---|---|
| theHarvester | Email, subdomain, and name harvesting from public sources | Standard OSINT starting point |
| SpiderFoot | Automated OSINT with a web UI | Visual map of an attack surface |
| Recon-ng | Modular OSINT framework | Script and repeat recon |
| Shodan | Internet-connected device search engine | Use the CLI for scripting |
| Censys | Certificate and host search | Often finds things Shodan misses |

### Git & code recon

| Tool | Purpose | When to use |
|---|---|---|
| GitHacker | Git source-leak exploitation | When you find an exposed `.git` directory |
| Gitrob | Reconnaissance tool for GitHub organizations | Find sensitive files across all repos in an org |
| GitGot | Semi-automated GitHub secret search | Large-scale secret hunting |
| TruffleHog | Secret scanner for git history | Standard for finding leaked credentials |
| Gitleaks | Fast secret scanner for git repos | Lighter than TruffleHog for CI integration |

---

## Web Application Security

### Scanning & fuzzing

| Tool | Purpose | When to use |
|---|---|---|
| Burp Suite Community | Standard web proxy | Free tier covers most manual work |
| OWASP ZAP | Open-source web app scanner | Automation without a Burp license |
| Nuclei | Template-based vulnerability scanner | CVE-specific checks at scale |
| ffuf | Fast web fuzzer | Directory, parameter, and vhost discovery |
| feroxbuster | Recursive content discovery | Faster than gobuster for deep directory trees |
| gobuster | Directory and DNS brute-forcer | Reliable and simple |
| wpscan | WordPress vulnerability scanner | The only tool you need for WP targets |

### XSS & injection

| Tool | Purpose | When to use |
|---|---|---|
| dalfox | Automated XSS scanner with parameter analysis | Best-in-class for XSS discovery |
| sqlmap | Automated SQL injection | Standard for confirmed SQLi exploitation |

### API testing

| Tool | Purpose | When to use |
|---|---|---|
| Postman | API client with testing capabilities | Free tier covers most needs |
| mitmproxy | Interactive HTTPS proxy | Script traffic manipulation |
| jwt_tool | JWT testing toolkit | Standard for JWT attack vectors |

---

## Network & Infrastructure

### Scanning & enumeration

| Tool | Purpose | When to use |
|---|---|---|
| Masscan | Internet-scale TCP port scanner | See Reconnaissance |
| RustScan | Modern port scanner | See Reconnaissance |
| SX | Fast modern network scanner | Large internal ranges |

### Vulnerability scanning

| Tool | Purpose | When to use |
|---|---|---|
| OpenVAS / Greenbone | Open-source vulnerability scanner | Free alternative to Nessus |
| Nexpose Community | Free tier of Rapid7's scanner | Limited but useful for small environments |

### Wireless

| Tool | Purpose | When to use |
|---|---|---|
| Aircrack-ng | WiFi security auditing suite | Standard for wireless assessments |
| Kismet | Wireless network detector and sniffer | Passive wireless recon |
| Wifite2 | Automated wireless attack tool | Quick WPA/WPA2 assessments |

### Database assessment

| Tool | Purpose | When to use |
|---|---|---|
| sqlmap | Automated SQL injection | See Web Application Security |

---

## Identity & Access

### Active Directory

| Tool | Purpose | When to use |
|---|---|---|
| BloodHound | AD attack path analysis | The single most important AD tool |
| Certipy | AD CS enumeration and abuse | Certificate-based attacks |
| Rubeus | Kerberos interaction and abuse | Standard for ticket manipulation |
| NetExec | Network execution and post-exploitation | Maintained successor to CrackMapExec |
| Impacket | Network protocol toolkit | Foundation library for most AD attacks |
| Responder | LLMNR/NBT-NS/MDNS poisoner | First tool to run on an internal network |
| Mimikatz | Credential extraction | *Reference only. Use with extreme caution and only in authorized engagements.* |

### Password attacks

| Tool | Purpose | When to use |
|---|---|---|
| Hashcat | GPU-accelerated password cracking | Standard for offline cracking |
| John the Ripper | CPU-based password cracker | Quick jobs without GPU access |
| Hydra | Network login brute-forcer | Online password attacks |
| CrackStation | Online hash lookup | Quick check before spinning up Hashcat |

---

## Exploitation & Post-Exploitation

### Frameworks

| Tool | Purpose | When to use |
|---|---|---|
| Metasploit Framework | Standard exploitation framework | Validated exploits and post-ex modules |
| Sliver | Modern C2 framework | *C2 framework. Use only in authorized engagements.* |
| Havoc | Modern C2 with a focus on evasion | *C2 framework. Use only in authorized engagements.* |
| Mythic | Collaborative C2 framework | *C2 framework. Use only in authorized engagements.* |
| Caldera | Automated adversary emulation | Purple team exercises |

### Privilege escalation

| Tool | Purpose | When to use |
|---|---|---|
| PEASS-ng | Privilege escalation scripts (WinPEAS, LinPEAS) | First tool to run after initial access |
| PowerUp | Windows privilege escalation | Part of PowerSploit |

### Tunneling & exfiltration

| Tool | Purpose | When to use |
|---|---|---|
| Chisel | TCP/UDP tunnel over HTTP | Pivoting through restrictive networks |
| Ligolo-ng | Reverse tunneling tool | Better than Chisel for complex pivots |
| DNScat2 | DNS tunneling | When all other channels are blocked |

---

## Container & Kubernetes Security

| Tool | Purpose | When to use |
|---|---|---|
| Prowler | Multi-cloud security posture auditing (AWS, Azure, GCP, Kubernetes) | Standard for cloud posture assessments |
| Trivy | Vulnerability and misconfiguration scanner for containers, IaC, and SBOMs | Runs in CI pipelines |
| Kubescape | Kubernetes security posture management with NSA-CISA hardening guidance | Built-in compliance checks |
| kube-bench | CIS Kubernetes Benchmark checks as a CLI tool | Run against every cluster |
| Checkov | Policy-as-code scanning for Terraform, CloudFormation, Kubernetes manifests | IaC review in CI |
| kube-hunter | Offensive-style Kubernetes cluster probing | Finds exposed services and weak configurations |
| peirates | Kubernetes penetration testing toolkit | Authorized cluster assessments |
| Falco | Runtime security monitoring for Linux hosts and Kubernetes | Standard for runtime detection |
| Tracee | Runtime security and forensics using eBPF | Deep Linux visibility |
| Tetragon | eBPF-based security observability and runtime enforcement | Part of the Cilium ecosystem |

---

## AI / LLM Security

### Scanning & testing

| Tool | Purpose | When to use |
|---|---|---|
| Garak | LLM vulnerability scanner | Standard for probing models for jailbreaks, injection, and leakage |
| PyRIT | AI red-teaming toolkit from Microsoft | Structured multi-turn attacks |
| LLM Guard | Input/output scanner for LLM applications | Sanitize prompts and completions in production |
| Rebuff | Prompt injection detection | Lightweight alternative to LLM Guard |
| Vigil | LLM security scanner with YARA-style rules | Custom detection logic |
| ModelScan | ML model file scanner | Supply-chain security of model artifacts |
| Fickling | Pickle analysis and decompilation | Audit `.pkl` model files |
| Giskard | ML model testing framework | Bias, robustness, and drift testing |

### Frameworks & references

| Tool | Purpose | When to use |
|---|---|---|
| OWASP LLM Top 10 | Canonical list of LLM application risks | Required reading for LLM-powered apps |
| MITRE ATLAS | Adversarial ML threat matrix | Map real incidents to techniques |
| NeMo Guardrails | Programmable guardrails for LLM applications | Building production LLM systems |
| Adversarial Robustness Toolbox | IBM's library for adversarial ML | Academic-grade but practical |

---

## Cloud Security Posture

| Tool | Purpose | When to use |
|---|---|---|
| Prowler | Multi-cloud security posture auditing | See Container & Kubernetes Security |
| CloudCustodian | Cloud governance engine | Policy-as-code across AWS, Azure, and GCP |
| ScoutSuite | Multi-cloud security auditing | Alternative to Prowler for quick assessments |
| Cloudsplaining | AWS IAM security assessment | IAM-specific deep dives |
| Pacu | AWS exploitation framework | Authorized AWS red team work |
| cdk-nag | AWS CDK construct library for security best-practice checks | CDK development in CI |

---

## Supply Chain Security

| Tool | Purpose | When to use |
|---|---|---|
| Syft | SBOM generator for containers and filesystems | Inventory what's in your artifacts |
| Grype | Vulnerability scanner for SBOMs | Pair with Syft |
| OSV-Scanner | Vulnerability scanner using the OSV database | Cross-ecosystem checks |
| GUAC | Supply-chain security graph | Deep dependency analysis |
| Sigstore | Signing and verification infrastructure | Standard for artifact signing |
| in-toto | Supply-chain integrity framework | Attest build steps |
| OpenSSF Scorecard | Automated security health checks for open-source projects | Run against your dependencies |
| CycloneDX | SBOM standard and tooling | SBOM generation and analysis |
| SPDX | SBOM standard from the Linux Foundation | Alternative to CycloneDX |
| SLSA | Supply-chain security framework | Assess and improve build integrity |

---

## Detection Engineering & DFIR

### Detection rules & testing

| Tool | Purpose | When to use |
|---|---|---|
| Sigma | Generic signature format for SIEMs | Standard for detection-as-code |
| YARA | Pattern matching for malware research | File-based detection |
| Atomic Red Team | MITRE ATT&CK technique tests | Validate detection coverage |
| Elastic Detection Rules | Pre-built rules for Elastic Security | Reference for Elastic users |
| Splunk Security Content | Detection content for Splunk | Reference for Splunk users |

### SIEM & XDR

| Tool | Purpose | When to use |
|---|---|---|
| Wazuh | Open-source XDR and SIEM | Self-hosted detection |
| Suricata | Network IDS/IPS | Standard for network-based detection |
| Zeek | Network security monitor | Deep network visibility |
| Velociraptor | Endpoint monitoring and DFIR | Standard for endpoint forensics |
| OSQuery | SQL-based endpoint instrumentation | Fleet-wide queries |

### Incident response

| Tool | Purpose | When to use |
|---|---|---|
| TheHive | Incident response platform | Case management |
| Cortex | Observable analysis engine | Pair with TheHive |
| MISP | Threat intelligence sharing | IoC management and sharing |
| Timesketch | Collaborative forensic timeline analysis | Large-scale timeline work |
| Plaso | Log2Timeline for forensic timeline extraction | Foundation tool for timeline analysis |
| KAPE | Artifact collection | Rapid triage collection |

---

## Reporting & Collaboration

| Tool | Purpose | When to use |
|---|---|---|
| Dradis | Reporting and collaboration platform for security teams | Team-based assessments |
| Faraday | Collaborative penetration test platform | Multi-person engagements |
| PlexTrac | Reporting and collaboration platform | Commercial, with a free tier |
| Ghostwriter | Reporting and operations platform | Red team operations |
| Serpico | Penetration test report generator | Lightweight alternative to Dradis |

---

## Distributions & Cyber Ranges

| Tool | Purpose | When to use |
|---|---|---|
| Kali Linux | Standard penetration testing distribution | Default choice for most work |
| Parrot Security | Security-focused Linux distribution | Alternative to Kali |
| BlackArch | Arch-based penetration testing distribution | If you prefer Arch |
| PentestBox | Windows-based pentesting environment | When you can't run Linux |
| Commando VM | Windows-based offensive VM from Mandiant | AD-focused work |
| Windows11 Penetration Suite | Windows 11-based pentesting toolkit | Windows-native testing |
| GOAD | Game of Active Directory | Practice lab for AD attacks |
| DetectionLab | Windows-based detection lab | Practice defensive tooling |
| PurpleTeamCloud | Cloud-based purple team lab | Cloud-native practice |

---

## Archived but useful

Tools that are no longer actively maintained but still work. Use them knowing they may break without warning.

| Tool | Purpose | When to use |
|---|---|---|
| Sublist3r | Subdomain enumeration via search engines | Second source for subdomain discovery. Unmaintained since 2020. |
| XSStrike | XSS detection suite with WAF bypass | Manual XSS testing. Unmaintained since 2021. |
| NoSQLMap | NoSQL injection testing | The only serious NoSQL injection tool. Unmaintained since 2021. |
| LinEnum | Linux enumeration script | Checklist for Linux privilege escalation. Unmaintained since 2019. |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Found something broken or missing? Open an issue or a PR.

## License

[MIT](LICENSE)
