# Submit AgentShare to awesome-mcp-servers (one-shot after gh login).
# 1) gh auth login -h github.com
# 2) powershell -ExecutionPolicy Bypass -File scripts/submit-awesome-mcp.ps1

$ErrorActionPreference = "Stop"
$workDir = "D:\awesome-mcp-servers"
$branch = "add-anhmtk-agentshare-mcp"
$upstream = "punkpeye/awesome-mcp-servers"

gh auth status -h github.com | Out-Null
if ($LASTEXITCODE -ne 0) {
    Write-Error "Run: gh auth login -h github.com"
}

if (-not (Test-Path $workDir)) {
    Write-Error "Missing $workDir - clone awesome-mcp-servers first."
}

Set-Location $workDir
git checkout $branch

$login = gh api user --jq .login

# Ensure fork exists (ignore "already exists" on stderr)
$forkOut = gh repo fork $upstream --remote=false 2>&1
if ($LASTEXITCODE -ne 0 -and ($forkOut -notmatch "already exists")) {
    throw "gh repo fork failed: $forkOut"
}
git remote get-url origin 2>$null | Out-Null
if ($LASTEXITCODE -ne 0) {
    git remote add origin "https://github.com/$login/awesome-mcp-servers.git"
} else {
    $originUrl = git remote get-url origin
    if ($originUrl -notmatch $login) {
        git remote set-url origin "https://github.com/$login/awesome-mcp-servers.git"
    }
}

git push -u origin $branch

$body = @(
    "## Summary"
    "- Add AgentShare MCP to E-Commerce section (alphabetical)."
    "- 10 tools: marketplace prices, ACP commerce_quote, DefiLlama DEX, Solana and Meteora briefs."
    "- Hosted at https://agentshare.dev/mcp"
    "- Repo: https://github.com/anhmtk/agentshare-mcp"
    "- Glama: https://glama.ai/mcp/servers/anhmtk/agentshare-mcp"
    ""
    "## Test plan"
    "- [x] Line inserted alphabetically after agentlux, before BuyWhere"
    "- [x] Glama badge URL matches listing"
    "- [x] Emojis included"
) -join "`n"

$title = "Add anhmtk/agentshare-mcp (AgentShare commerce price MCP)"
gh pr create --repo $upstream --head "${login}:${branch}" --title $title --body $body

Write-Host ""
Write-Host "Done. Open the PR URL above on GitHub."
