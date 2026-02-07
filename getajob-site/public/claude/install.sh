#!/bin/bash

# GetAJob Skill Installer (Claude.ai)
# https://getajob.hackeroos.com.au

set -e

ORANGE='\033[0;33m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo -e "${ORANGE}╔═══════════════════════════════════════════╗${NC}"
echo -e "${ORANGE}║${NC}     🦘 ${CYAN}GetAJob${NC} — Claude AI Skill          ${ORANGE}║${NC}"
echo -e "${ORANGE}╚═══════════════════════════════════════════╝${NC}"
echo ""

INSTALL_DIR="$HOME/get-a-job-claude"

echo -e "${ORANGE}→${NC} Installing to ${INSTALL_DIR}..."

mkdir -p "$INSTALL_DIR/scripts"
mkdir -p "$INSTALL_DIR/references"

BASE_URL="https://getajob.hackeroos.com.au/claude/skill"

echo -e "${ORANGE}→${NC} Downloading skill files..."

curl -fsSL "$BASE_URL/SKILL.md" -o "$INSTALL_DIR/SKILL.md"
curl -fsSL "$BASE_URL/scripts/init_workspace.py" -o "$INSTALL_DIR/scripts/init_workspace.py"
curl -fsSL "$BASE_URL/scripts/add_listing.py" -o "$INSTALL_DIR/scripts/add_listing.py"
curl -fsSL "$BASE_URL/scripts/update_dream_company.py" -o "$INSTALL_DIR/scripts/update_dream_company.py"
curl -fsSL "$BASE_URL/references/search-strategies.md" -o "$INSTALL_DIR/references/search-strategies.md"
curl -fsSL "$BASE_URL/references/csv-schemas.md" -o "$INSTALL_DIR/references/csv-schemas.md"
curl -fsSL "$BASE_URL/references/application-materials.md" -o "$INSTALL_DIR/references/application-materials.md"
curl -fsSL "$BASE_URL/references/summary-templates.md" -o "$INSTALL_DIR/references/summary-templates.md"

chmod +x "$INSTALL_DIR/scripts/"*.py 2>/dev/null || true

echo ""
echo -e "${GREEN}✓ Installation complete!${NC}"
echo ""
echo -e "  ${CYAN}Skill installed to:${NC} $INSTALL_DIR"
echo ""
echo -e "  ${ORANGE}Next steps:${NC}"
echo "  1. Open claude.ai and start a new conversation"
echo "  2. Upload the SKILL.md file"
echo "  3. Say: \"Use this skill to help me find a job\""
echo "  4. Then say: \"Set up my job search\""
echo ""
echo -e "  ${GREEN}Happy job hunting! 🎯${NC}"
echo ""
