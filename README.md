# sec-toolkit

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Link Check](https://github.com/Bimpebabs/sec-toolkit/workflows/Link%20Check/badge.svg)](https://github.com/Bimpebabs/sec-toolkit/actions/workflows/link-check.yml)
[![Staleness Check](https://github.com/Bimpebabs/sec-toolkit/workflows/Staleness%20Check/badge.svg)](https://github.com/Bimpebabs/sec-toolkit/actions/workflows/staleness-check.yml)
[![Last Commit](https://img.shields.io/github/last-commit/Bimpebabs/sec-toolkit)](https://github.com/Bimpebabs/sec-toolkit/commits/main)

> A curated list of the best open-source penetration testing tools, red team tools, blue team tools, and incident response tools for security professionals. Organized by engagement phase, with a practitioner's note on when to reach for each one.

**Why this list exists.** Most cybersecurity tool lists are either offense-only or a flat dump of links with no context. This one covers the full engagement lifecycle from reconnaissance through detection engineering and DFIR. Every entry has a one-line note on when to reach for it, written from real use in penetration testing, red team operations, and incident response.

**Scope.** Tools you'd reach for during authorized work: penetration tests, red team engagements, purple team exercises, security assessments, vulnerability assessments, and incident response. Defensive security tools are first-class because modern engagements are rarely offense-only.

**Not included.** Commercial-only tools, tools with no public source or distribution, anything primarily malicious in intent. Dual-use tools are included with context.

**Keywords:** penetration testing tools, red team tools, blue team tools, incident response tools, cybersecurity tools, open source security tools, offensive security tools, defensive security tools, DFIR tools, vulnerability assessment tools, AD security tools, cloud security tools, AI security tools, LLM security tools, supply chain security tools, detection engineering, Kubernetes security tools

---

## Quick start

New here? These are the tools I'd install first on a fresh machine for penetration testing or incident response.

| Phase | Tool | Why |
|---|---|---|
| Recon | [Subfinder](https://github.com/projectdiscovery/subfinder) | Passive subdomain discovery. First thing to run on any engagement. |
| Recon | [httpx](https://github.com/projectdiscovery/httpx) | Validate which subdomains are actually live. |
| Web | [Burp Suite Community](https://portswigger.net/burp/communitydownload) | The standard web proxy. Free tier covers most manual work. |
| Web | [Nuclei](https://github.com/projectdiscovery/nuclei) | Template-based vulnerability scanning at scale. |
| AD | [BloodHound](https://github.com/SpecterOps/BloodHound) | AD attack path analysis. The single most important AD tool. |
| AD | [NetExec](https://github.com/Pennyw0rth/NetExec) | Network execution. The maintained successor to CrackMapExec. |
| Container | [Trivy](https://github.com/aquasecurity/trivy) | Container and IaC vulnerability scanning. Runs in CI. |
| AI | [Garak](https://github.com/NVIDIA/garak) | LLM vulnerability scanner. The standard for probing models. |
| Supply chain | [Syft](https://github.com/anchore/syft) + [Grype](https://github.com/anchore/grype) | SBOM generation and vulnerability scanning. |
| Detection | [Sigma](https://github.com/SigmaHQ/sigma) | Detection-as-code. The standard format for SIEM rules. |

---

## Contents

- [Reconnaissance & OSINT](#reconnaissance--osint)
- [Web Application Security](#web-application-security)
- [Network & Infrastructure](#network--infrastructure)
- [Identity & Access](#identity--access)
- [Exploitation & Post-Exploitation](#exploitation--post-exploitation)
- [Container & Kubernetes Security](#container--kubernetes-security)
- [AI / LLM Security](#ai--llm-security)
- [Cloud Security Posture](#cloud-security-posture)
- [Supply Chain Security](#supply-chain-security)
- [Detection Engineering & DFIR](#detection-engineering--dfir)
- [Reporting & Collaboration](#reporting--collaboration)
- [Distributions & Cyber Ranges](#distributions--cyber-ranges)

---

## Reconnaissance & OSINT

### Subdomain & DNS enumeration

| Tool | Description | When to reach for it |
|---|---|---|
| [Subfinder](https://github.com/projectdiscovery/subfinder) | Passive subdomain discovery from dozens of sources. | First tool to run on any new engagement. |
| [Amass](https://github.com/OWASP/Amass) | In-depth attack surface mapping with graph output. | When Subfinder alone isn't enough. |
| [dnsx](https://github.com/projectdiscovery/dnsx) | Fast multi-purpose DNS toolkit. | Resolve and validate large subdomain lists. |
| [httpx](https://github.com/projectdiscovery/httpx) | HTTP prober for validating live hosts. | Pair with Subfinder to confirm which subdomains respond. |
| [katana](https://github.com/projectdiscovery/katana) | Web crawler with headless-browser support. | Better than `gau` for modern JS-heavy apps. |
| [gau](https://github.com/lc/gau) | Fetch known URLs from AlienVault, Wayback Machine, Common Crawl. | Quick historical URL discovery. |
| [waybackurls](https://github.com/tomnomnom/waybackurls) | Wayback Machine URL fetcher. | Lightweight alternative to gau. |
| [Sublist3r](https://github.com/aboul3la/Sublist3r) | Subdomain enumeration via search engines. | *Unmaintained since 2020. Still works as a second source.* |

### Port scanning

| Tool | Description | When to reach for it |
|---|---|---|
| [Nmap](https://nmap.org/) | The standard network scanner. | Deep service detection and NSE scripting. |
| [Masscan](https://github.com/robertdavidgraham/masscan) | Internet-scale TCP port scanner. | Large ranges, then hand off to Nmap for service detection. |
| [Naabu](https://github.com/projectdiscovery/naabu) | Fast, reliable port scanner written in Go. | Middle ground between Masscan and Nmap. |
| [RustScan](https://github.com/RustScan/RustScan) | Modern port scanner that pipes into Nmap. | Fast for CTFs and quick assessments. |

### Search engines & threat intel

| Tool | Description | When to reach for it |
|---|---|---|
| [theHarvester](https://github.com/laramies/theHarvester) | Email, subdomain, and name harvesting from public sources. | Standard OSINT starting point. |
| [SpiderFoot](https://github.com/smicallef/spiderfoot) | Automated OSINT with a web UI. | When you want a visual map of an attack surface. |
| [Recon-ng](https://github.com/lanmaster53/recon-ng) | Modular OSINT framework. | When you want to script and repeat recon. |
| [Shodan](https://www.shodan.io/) | Internet-connected device search engine. | Use the CLI for scripting. |
| [Censys](https://search.censys.io/) | Certificate and host search. | Often finds things Shodan misses. |

### Git & code recon

| Tool | Description | When to reach for it |
|---|---|---|
| [GitHacker](https://github.com/WangYihang/GitHacker) | Git source-leak exploitation. | When you find an exposed `.git` directory. |
| [Gitrob](https://github.com/michenriksen/gitrob) | Reconnaissance tool for GitHub organizations. | Finds sensitive files across all repos in an org. |
| [GitGot](https://github.com/BishopFox/GitGot) | Semi-automated GitHub secret search. | Large-scale secret hunting. |
| [TruffleHog](https://github.com/trufflesecurity/trufflehog) | Secret scanner for git history. | The standard for finding leaked credentials. |
| [Gitleaks](https://github.com/gitleaks/gitleaks) | Fast secret scanner for git repos. | Lighter than TruffleHog for CI integration. |

---

## Web Application Security

### Scanning & fuzzing

| Tool | Description | When to reach for it |
|---|---|---|
| [Burp Suite Community](https://portswigger.net/burp/communitydownload) | The standard web proxy. | Free tier is enough for most manual work. |
| [OWASP ZAP](https://github.com/zaproxy/zaproxy) | Open-source web app scanner. | When you need automation without a Burp license. |
| [Nuclei](https://github.com/projectdiscovery/nuclei) | Template-based vulnerability scanner. | CVE-specific checks at scale. |
| [ffuf](https://github.com/ffuf/ffuf) | Fast web fuzzer. | Directory, parameter, and vhost discovery. |
| [feroxbuster](https://github.com/epi052/feroxbuster) | Recursive content discovery. | Faster than gobuster for deep directory trees. |
| [gobuster](https://github.com/OJ/gobuster) | Directory and DNS brute-forcer. | Reliable and simple. |
| [wpscan](https://github.com/wpscanteam/wpscan) | WordPress vulnerability scanner. | The only tool you need for WP targets. |

### XSS & injection

| Tool | Description | When to reach for it |
|---|---|---|
| [dalfox](https://github.com/hahwul/dalfox) | Automated XSS scanner with parameter analysis. | Best-in-class for XSS discovery. |
| [XSStrike](https://github.com/s0md3v/XSStrike) | XSS detection suite with WAF bypass. | *Unmaintained since 2021. Still useful for manual testing.* |
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | Automated SQL injection. | The standard for confirmed SQLi exploitation. |
| [NoSQLMap](https://github.com/codingo/NoSQLMap) | NoSQL injection testing. | *Unmaintained since 2021. Still the only serious NoSQL injection tool.* |

### API testing

| Tool | Description | When to reach for it |
|---|---|---|
| [Postman](https://www.postman.com/) | API client with testing capabilities. | Free tier covers most needs. |
| [mitmproxy](https://github.com/mitmproxy/mitmproxy) | Interactive HTTPS proxy. | When you need to script traffic manipulation. |
| [jwt_tool](https://github.com/ticarpi/jwt_tool) | JWT testing toolkit. | The standard for JWT attack vectors. |

---

## Network & Infrastructure

### Scanning & enumeration

| Tool | Description | When to reach for it |
|---|---|---|
| [Masscan](https://github.com/robertdavidgraham/masscan) | Internet-scale TCP port scanner. | See Reconnaissance. |
| [RustScan](https://github.com/RustScan/RustScan) | Modern port scanner. | See Reconnaissance. |
| [SX](https://github.com/v-byte-cpu/sx) | Fast modern network scanner. | Large internal ranges. |

### Vulnerability scanning

| Tool | Description | When to reach for it |
|---|---|---|
| [OpenVAS / Greenbone](https://github.com/greenbone/openvas-scanner) | Open-source vulnerability scanner. | The free alternative to Nessus. |
| [Nexpose Community](https://www.rapid7.com/products/nexpose/) | Free tier of Rapid7's scanner. | Limited but useful for small environments. |

### Wireless

| Tool | Description | When to reach for it |
|---|---|---|
| [Aircrack-ng](https://github.com/aircrack-ng/aircrack-ng) | WiFi security auditing suite. | The standard for wireless assessments. |
| [Kismet](https://github.com/kismetwireless/kismet) | Wireless network detector and sniffer. | Passive wireless recon. |
| [Wifite2](https://github.com/derv82/wifite2) | Automated wireless attack tool. | Quick WPA/WPA2 assessments. |

### Database assessment

| Tool | Description | When to reach for it |
|---|---|---|
| [sqlmap](https://github.com/sqlmapproject/sqlmap) | Automated SQL injection. | See Web Application Security. |
| [NoSQLMap](https://github.com/codingo/NoSQLMap) | NoSQL injection testing. | See Web Application Security. |

---

## Identity & Access

### Active Directory

| Tool | Description | When to reach for it |
|---|---|---|
| [BloodHound](https://github.com/SpecterOps/BloodHound) | AD attack path analysis. | The single most important AD tool. |
| [Certipy](https://github.com/ly4k/Certipy) | AD CS enumeration and abuse. | Certificate-based attacks. |
| [Rubeus](https://github.com/GhostPack/Rubeus) | Kerberos interaction and abuse. | Standard for ticket manipulation. |
| [NetExec](https://github.com/Pennyw0rth/NetExec) | Network execution and post-exploitation. | The maintained successor to CrackMapExec. |
| [Impacket](https://github.com/fortra/impacket) | Network protocol toolkit. | Foundation library for most AD attacks. |
| [Responder](https://github.com/lgandx/Responder) | LLMNR/NBT-NS/MDNS poisoner. | First tool to run on an internal network. |
| [Mimikatz](https://github.com/gentilkiwi/mimikatz) | Credential extraction. | *Reference only. Use with extreme caution and only in authorized engagements.* |

### Password attacks

| Tool | Description | When to reach for it |
|---|---|---|
| [Hashcat](https://github.com/hashcat/hashcat) | GPU-accelerated password cracking. | The standard for offline cracking. |
| [John the Ripper](https://github.com/openwall/john) | CPU-based password cracker. | Quick jobs without GPU access. |
| [Hydra](https://github.com/vanhauser-thc/thc-hydra) | Network login brute-forcer. | Online password attacks. |
| [CrackStation](https://crackstation.net/) | Online hash lookup. | Quick check before spinning up Hashcat. |

---

## Exploitation & Post-Exploitation

### Frameworks

| Tool | Description | When to reach for it |
|---|---|---|
| [Metasploit Framework](https://github.com/rapid7/metasploit-framework) | The standard exploitation framework. | Validated exploits and post-ex modules. |
| [Sliver](https://github.com/BishopFox/sliver) | Modern C2 framework. | *C2 framework. Use only in authorized engagements.* |
| [Havoc](https://github.com/HavocFramework/Havoc) | Modern C2 with a focus on evasion. | *C2 framework. Use only in authorized engagements.* |
| [Mythic](https://github.com/its-a-feature/Mythic) | Collaborative C2 framework. | *C2 framework. Use only in authorized engagements.* |
| [Caldera](https://github.com/mitre/caldera) | Automated adversary emulation. | Purple team exercises. |

### Privilege escalation

| Tool | Description | When to reach for it |
|---|---|---|
| [PEASS-ng](https://github.com/peass-ng/PEASS-ng) | Privilege escalation scripts (WinPEAS, LinPEAS). | First tool to run after initial access. |
| [PowerUp](https://github.com/PowerShellMafia/PowerSploit) | Windows privilege escalation. | Part of PowerSploit. |
| [LinEnum](https://github.com/rebootuser/LinEnum) | Linux enumeration script. | *Unmaintained since 2019. Still useful as a checklist.* |

### Tunneling & exfiltration

| Tool | Description | When to reach for it |
|---|---|---|
| [Chisel](https://github.com/jpillora/chisel) | TCP/UDP tunnel over HTTP. | Pivoting through restrictive networks. |
| [Ligolo-ng](https://github.com/nicocha30/ligolo-ng) | Reverse tunneling tool. | Better than Chisel for complex pivots. |
| [DNScat2](https://github.com/iagox86/dnscat2) | DNS tunneling. | When all other channels are blocked. |

---

## Container & Kubernetes Security

| Tool | Description | When to reach for it |
|---|---|---|
| [Prowler](https://github.com/prowler-cloud/prowler) | Multi-cloud security posture auditing (AWS, Azure, GCP, Kubernetes). | The standard for cloud posture assessments. |
| [Trivy](https://github.com/aquasecurity/trivy) | Vulnerability and misconfiguration scanner for containers, IaC, and SBOMs. | Runs in CI pipelines. |
| [Kubescape](https://github.com/kubescape/kubescape) | Kubernetes security posture management with NSA-CISA hardening guidance. | Built-in compliance checks. |
| [kube-bench](https://github.com/aquasecurity/kube-bench) | CIS Kubernetes Benchmark checks as a CLI tool. | Run against every cluster you touch. |
| [Checkov](https://github.com/bridgecrewio/checkov) | Policy-as-code scanning for Terraform, CloudFormation, Kubernetes manifests. | IaC review in CI. |
| [kube-hunter](https://github.com/aquasecurity/kube-hunter) | Offensive-style Kubernetes cluster probing. | Finds exposed services and weak configurations. |
| [peirates](https://github.com/inguardians/peirates) | Kubernetes penetration testing toolkit. | Authorized cluster assessments. |
| [Falco](https://github.com/falcosecurity/falco) | Runtime security monitoring for Linux hosts and Kubernetes. | The standard for runtime detection. |
| [Tracee](https://github.com/aquasecurity/tracee) | Runtime security and forensics using eBPF. | Deep Linux visibility. |
| [Tetragon](https://github.com/cilium/tetragon) | eBPF-based security observability and runtime enforcement. | Part of the Cilium ecosystem. |

---

## AI / LLM Security

### Scanning & testing

| Tool | Description | When to reach for it |
|---|---|---|
| [Garak](https://github.com/NVIDIA/garak) | LLM vulnerability scanner. | The standard for probing models for jailbreaks, injection, and leakage. |
| [PyRIT](https://github.com/Azure/PyRIT) | AI red-teaming toolkit from Microsoft. | Structured multi-turn attacks. |
| [LLM Guard](https://github.com/protectai/llm-guard) | Input/output scanner for LLM applications. | Sanitize prompts and completions in production. |
| [Rebuff](https://github.com/protectai/rebuff) | Prompt injection detection. | Lightweight alternative to LLM Guard. |
| [Vigil](https://github.com/deadbits/vigil-llm) | LLM security scanner with YARA-style rules. | Custom detection logic. |
| [ModelScan](https://github.com/protectai/modelscan) | ML model file scanner. | Supply-chain security of model artifacts. |
| [Fickling](https://github.com/trailofbits/fickling) | Pickle analysis and decompilation. | Audit `.pkl` model files. |
| [Giskard](https://github.com/Giskard-AI/giskard) | ML model testing framework. | Bias, robustness, and drift testing. |

### Frameworks & references

| Tool | Description | When to reach for it |
|---|---|---|
| [OWASP LLM Top 10](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications) | The canonical list of LLM application risks. | Required reading for anyone building LLM-powered apps. |
| [MITRE ATLAS](https://github.com/mitre-atlas) | Adversarial ML threat matrix. | Map real incidents to techniques. |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | Programmable guardrails for LLM applications. | Building production LLM systems. |
| [Adversarial Robustness Toolbox](https://github.com/Trusted-AI/adversarial-robustness-toolbox) | IBM's library for adversarial ML. | Academic-grade but practical. |

---

## Cloud Security Posture

| Tool | Description | When to reach for it |
|---|---|---|
| [Prowler](https://github.com/prowler-cloud/prowler) | Multi-cloud security posture auditing. | See Container & Kubernetes Security. |
| [CloudCustodian](https://github.com/cloud-custodian/cloud-custodian) | Cloud governance engine. | Policy-as-code across AWS, Azure, and GCP. |
| [ScoutSuite](https://github.com/nccgroup/ScoutSuite) | Multi-cloud security auditing. | Alternative to Prowler for quick assessments. |
| [Cloudsplaining](https://github.com/salesforce/cloudsplaining) | AWS IAM security assessment. | IAM-specific deep dives. |
| [Pacu](https://github.com/RhinoSecurityLabs/pacu) | AWS exploitation framework. | Authorized AWS red team work. |
| [cdk-nag](https://github.com/cdklabs/cdk-nag) | AWS CDK construct library for security best-practice checks. | CDK development in CI. |

---

## Supply Chain Security

| Tool | Description | When to reach for it |
|---|---|---|
| [Syft](https://github.com/anchore/syft) | SBOM generator for containers and filesystems. | Inventory what's in your artifacts. |
| [Grype](https://github.com/anchore/grype) | Vulnerability scanner for SBOMs. | Pair with Syft. |
| [OSV-Scanner](https://github.com/google/osv-scanner) | Vulnerability scanner using the OSV database. | Cross-ecosystem checks. |
| [GUAC](https://github.com/guacsec/guac) | Supply-chain security graph. | Deep dependency analysis. |
| [Sigstore](https://github.com/sigstore) | Signing and verification infrastructure. | The standard for artifact signing. |
| [in-toto](https://github.com/in-toto) | Supply-chain integrity framework. | Attest build steps. |
| [OpenSSF Scorecard](https://github.com/ossf/scorecard) | Automated security health checks for open-source projects. | Run against your dependencies. |
| [CycloneDX](https://github.com/CycloneDX) | SBOM standard and tooling. | SBOM generation and analysis. |
| [SPDX](https://github.com/spdx) | SBOM standard from the Linux Foundation. | Alternative to CycloneDX. |
| [SLSA](https://slsa.dev/) | Supply-chain security framework. | Assess and improve build integrity. |

---

## Detection Engineering & DFIR

### Detection rules & testing

| Tool | Description | When to reach for it |
|---|---|---|
| [Sigma](https://github.com/SigmaHQ/sigma) | Generic signature format for SIEMs. | The standard for detection-as-code. |
| [YARA](https://github.com/VirusTotal/yara) | Pattern matching for malware research. | File-based detection. |
| [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) | MITRE ATT&CK technique tests. | Validate detection coverage. |
| [Elastic Detection Rules](https://github.com/elastic/detection-rules) | Pre-built rules for Elastic Security. | Good reference even if you don't use Elastic. |
| [Splunk Security Content](https://github.com/splunk/security_content) | Detection content for Splunk. | Good reference for Splunk shops. |

### SIEM & XDR

| Tool | Description | When to reach for it |
|---|---|---|
| [Wazuh](https://github.com/wazuh/wazuh) | Open-source XDR and SIEM. | Self-hosted detection. |
| [Suricata](https://github.com/OISF/suricata) | Network IDS/IPS. | The standard for network-based detection. |
| [Zeek](https://github.com/zeek/zeek) | Network security monitor. | Deep network visibility. |
| [Velociraptor](https://github.com/Velocidex/velociraptor) | Endpoint monitoring and DFIR. | The standard for endpoint forensics. |
| [OSQuery](https://github.com/osquery/osquery) | SQL-based endpoint instrumentation. | Fleet-wide queries. |

### Incident response

| Tool | Description | When to reach for it |
|---|---|---|
| [TheHive](https://github.com/TheHive-Project/TheHive) | Incident response platform. | Case management. |
| [Cortex](https://github.com/TheHive-Project/Cortex) | Observable analysis engine. | Pair with TheHive. |
| [MISP](https://github.com/MISP/MISP) | Threat intelligence sharing. | IoC management and sharing. |
| [Timesketch](https://github.com/google/timesketch) | Collaborative forensic timeline analysis. | Large-scale timeline work. |
| [Plaso](https://github.com/log2timeline/plaso) | Log2Timeline for forensic timeline extraction. | Foundation tool for timeline analysis. |
| [KAPE](https://www.kroll.com/en/insights/publications/cyber/kroll-artifact-parser-extractor-kape) | Artifact collection. | Rapid triage collection. |

---

## Reporting & Collaboration

| Tool | Description | When to reach for it |
|---|---|---|
| [Dradis](https://github.com/dradis/dradis-ce) | Reporting and collaboration platform for security teams. | Team-based assessments. |
| [Faraday](https://github.com/infobyte/faraday) | Collaborative penetration test platform. | Multi-person engagements. |
| [PlexTrac](https://plextrac.com/) | Reporting and collaboration platform. | Commercial, with a free tier. |
| [Ghostwriter](https://github.com/GhostManager/Ghostwriter) | Reporting and operations platform. | Red team operations. |
| [Serpico](https://github.com/SerpicoProject/Serpico) | Penetration test report generator. | Lightweight alternative to Dradis. |

---

## Distributions & Cyber Ranges

| Tool | Description | When to reach for it |
|---|---|---|
| [Kali Linux](https://www.kali.org/) | The standard penetration testing distribution. | Default choice for most work. |
| [Parrot Security](https://www.parrotsec.org/) | Security-focused Linux distribution. | Good alternative to Kali. |
| [BlackArch](https://blackarch.org/) | Arch-based penetration testing distribution. | If you prefer Arch. |
| [PentestBox](https://pentestbox.org/) | Windows-based pentesting environment. | When you can't run Linux. |
| [Commando VM](https://github.com/mandiant/commando-vm) | Windows-based offensive VM from Mandiant. | AD-focused work. |
| [Windows11 Penetration Suite](https://github.com/arch3rPro/Pentest-Windows) | Windows 11-based pentesting toolkit. | Windows-native testing. |
| [GOAD](https://github.com/Orange-Cyberdefense/GOAD) | Game of Active Directory. | Practice lab for AD attacks. |
| [DetectionLab](https://github.com/clong/DetectionLab) | Windows-based detection lab. | Practice defensive tooling. |
| [PurpleTeamCloud](https://github.com/chvancooten/PurpleTeamCloud) | Cloud-based purple team lab. | Cloud-native practice. |

---

## Contributing

Found a broken link? Know a tool that belongs here? See [CONTRIBUTING.md](CONTRIBUTING.md). It takes about two minutes to open an issue or a PR.

## License

[MIT](LICENSE). Use it, fork it, build on it.
