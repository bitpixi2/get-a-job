#!/bin/bash

# GetAJob Skill Installer (OpenClaw)
# https://getajob.bitpixi.com

set -e

ORANGE='\033[0;33m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

echo ""
echo -e "${ORANGE}╔═══════════════════════════════════════════╗${NC}"
echo -e "${ORANGE}║${NC}       ${CYAN}GetAJob${NC} — OpenClaw Skill           ${ORANGE}║${NC}"
echo -e "${ORANGE}╚═══════════════════════════════════════════╝${NC}"
echo ""

# OpenClaw skills go in ~/clawd/skills/
INSTALL_DIR="$HOME/get-a-job-openclaw"
SKILL_DIR="$HOME/clawd/skills/getajob"

echo -e "${ORANGE}→${NC} Installing to ${INSTALL_DIR}..."
echo -e "${ORANGE}→${NC} Linking to ${SKILL_DIR}..."

mkdir -p "$INSTALL_DIR"
mkdir -p "$HOME/clawd/skills"

BASE_URL="https://getajob.bitpixi.com/openclaw/skill"

echo -e "${ORANGE}→${NC} Downloading skill files..."

curl -fsSL "$BASE_URL/SKILL.md" -o "$INSTALL_DIR/SKILL.md"

# Create symlink for OpenClaw to find the skill
ln -sf "$INSTALL_DIR" "$SKILL_DIR" 2>/dev/null || cp -r "$INSTALL_DIR" "$SKILL_DIR"

echo ""
echo -e "${GREEN}✓ Installation complete!${NC}"
echo ""
echo -e "  ${CYAN}Skill installed to:${NC} $INSTALL_DIR"
echo -e "  ${CYAN}Linked to:${NC} $SKILL_DIR"
echo ""
echo -e "  ${ORANGE}Next steps:${NC}"
echo "  1. Restart OpenClaw gateway:"
echo "     openclaw gateway restart"
echo ""
echo "  2. Verify skill loaded:"
echo "     openclaw skills list"
echo ""
echo "  3. Message your agent:"
echo "     \"Set up my job search\""
echo ""
echo -e "  ${GREEN}Happy job hunting! 🎯${NC}"
echo ""
