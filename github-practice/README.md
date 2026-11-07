# Git & GitHub classroom practice — VS Code

This folder contains a small, original-to-this-portfolio Python exercise intended for a **student-performed** Git/GitHub workflow. It is a practical example, not simulated proof of a local Git operation.

**Notebook:** [power_of_two_git_practice.ipynb](power_of_two_git_practice.ipynb)

## Suggested evidence for the course submission

The assignment requires a report showing account/repository creation, Git installation, local/remote synchronization, VS Code commit/push/pull, a notebook upload, verification on the GitHub website, and a subsequent notebook change published in another commit. Use your existing seven-section Word report template and **capture your own actual screens**.

| Step | Perform on your Mac | Suggested screenshot |
| --- | --- | --- |
| 1 | Open your GitHub profile and the repository in the browser | Your GitHub account and repository address |
| 2 | In Terminal, run `git --version` | Installed Git version |
| 3 | Clone this repository locally (or use VS Code's **Clone Repository**) | Local clone and connected remote |
| 4 | Open the folder in VS Code, select Python kernel, run the notebook | Notebook and VS Code Source Control |
| 5 | Make a small change in the last code cell, save, stage and commit | Changed file and commit |
| 6 | Push and pull using VS Code's Source Control menu | Sync operations, with real output/status |
| 7 | Refresh the GitHub notebook page and inspect the commit history | Published notebook change and new commit hash |

## Commands (optional Terminal equivalent)

```bash
git clone https://github.com/SantiagoGlez12/python-learning-journey.git
cd python-learning-journey
git status
git pull origin main
```

Modify and save `github-practice/power_of_two_git_practice.ipynb` in VS Code. Then use VS Code's **Source Control → Stage Changes → Commit → Push/Sync Changes**, or the commands below:

```bash
git add github-practice/power_of_two_git_practice.ipynb
git commit -m "Update power-of-two notebook exercise"
git push origin main
```

If your local branch or repository rules differ, use the branch shown by `git branch --show-current`. Do not force-push. A screenshot of the GitHub commit history is evidence of successful publication, not merely a locally saved notebook.

**Important:** The initial notebook was committed from the connected assistant GitHub integration; it does **not** count as evidence that you personally ran Git/VS Code commands on your Mac. Your second, locally created commit and the screenshots are still required to complete the course report.

## Context

The mathematical task intentionally uses introductory control flow. It reuses the same learning concept as [the standalone Python function](../fundamentals/power_of_two.py) and adds a cell designed for a real follow-up edit. The notebook is a learning artifact, not a production application.
