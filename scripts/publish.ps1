param(
  [string]$repoName = "sentongo-web",
  [ValidateSet('public','private')][string]$visibility = "public"
)

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
  Write-Error "gh CLI not found. Install from https://github.com/cli/cli and authenticate (gh auth login)."
  exit 1
}

$vis = if ($visibility -eq 'public') { '--public' } else { '--private' }

gh repo create $repoName $vis --source . --remote origin --push
if ($LASTEXITCODE -ne 0) {
  Write-Error "Failed to create or push repository. Check gh output above."
  exit $LASTEXITCODE
}

Write-Host "Repository created and pushed as $repoName"
