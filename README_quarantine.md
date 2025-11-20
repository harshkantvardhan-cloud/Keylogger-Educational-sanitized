# Quarantine Notice

The original `keylogger.py` has been moved to `quarantine/keylogger_original.py` and replaced with a safe, simulated demo.

Recommended next steps:
- Run an antivirus scan (Windows Defender) and remove any unwanted files.
- Inspect autostart entries and scheduled tasks.
- Delete the quarantined file if you do not need it.

Windows Defender quick commands (run in an elevated PowerShell):
```powershell
Update-MpSignature
Start-MpScan -ScanType FullScan
```

If you want to convert this project into a safe learning exercise, I can:
- Replace the quarantined file with a simulated input visualizer.
- Add unit tests and documentation for event-handling patterns (no real logging).
- Or permanently delete the quarantined file.

Tell me which option you prefer.
