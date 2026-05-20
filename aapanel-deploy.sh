#!/usr/bin/env bash
# ════════════════════════════════════════════════════════════
# Vnstock.io.vn — One-shot deploy script (chạy TRÊN VPS aaPanel)
#
# Cách dùng (đơn giản nhất):
#   1. Upload file mới (index.html, landing.html, server.py,
#      app-proxy.conf, manifest.json, icons/...) vào
#      /www/wwwroot/vnstock.io.vn/ qua aaPanel File Manager
#   2. SSH vào VPS, chạy:
#        bash /www/wwwroot/vnstock.io.vn/aapanel-deploy.sh
#
# Script tự:
#   • Copy app-proxy.conf vào aaPanel extension dir
#   • Test nginx config — nếu fail thì rollback, KHÔNG ngắt web
#   • Reload nginx + restart Python (kill old + nohup new)
#   • Verify health endpoint
# ════════════════════════════════════════════════════════════
set -euo pipefail

WEBROOT="/www/wwwroot/vnstock.io.vn"
EXT_DIR="/www/server/panel/vhost/nginx/extension/vnstock.io.vn"
LOG="/var/log/sma.log"
HEALTH_URL="http://127.0.0.1:3333/health"

cd "$WEBROOT"

echo "──────────────────────────────────────────────"
echo "  Vnstock.io.vn deploy — $(date '+%F %T')"
echo "──────────────────────────────────────────────"

# 1. Copy app-proxy.conf vào extension dir nếu có file mới hơn
NGINX_CHANGED=0
if [ -f "$WEBROOT/app-proxy.conf" ]; then
  mkdir -p "$EXT_DIR"
  if ! diff -q "$WEBROOT/app-proxy.conf" "$EXT_DIR/app-proxy.conf" >/dev/null 2>&1; then
    # Backup file cũ trước khi đè
    [ -f "$EXT_DIR/app-proxy.conf" ] && cp "$EXT_DIR/app-proxy.conf" "$EXT_DIR/app-proxy.conf.bak"
    cp "$WEBROOT/app-proxy.conf" "$EXT_DIR/app-proxy.conf"
    echo "  ✓ Copied app-proxy.conf → extension dir"
    NGINX_CHANGED=1
  else
    echo "  • app-proxy.conf không đổi"
  fi
fi

# 2. Test + reload nginx (chỉ khi config có đổi)
if [ "$NGINX_CHANGED" = "1" ]; then
  if nginx -t 2>/dev/null; then
    nginx -s reload
    echo "  ✓ Nginx reloaded"
  else
    echo "  ❌ Nginx config FAIL — rollback file backup"
    nginx -t
    if [ -f "$EXT_DIR/app-proxy.conf.bak" ]; then
      mv "$EXT_DIR/app-proxy.conf.bak" "$EXT_DIR/app-proxy.conf"
      echo "  ✓ Đã rollback về file backup"
    else
      rm -f "$EXT_DIR/app-proxy.conf"
    fi
    exit 1
  fi
fi

# 3. Restart Python app
echo "  ► Restarting Python server..."
pkill -f "python3.*server.py" 2>/dev/null || true
sleep 2

# Verify venv
if [ ! -x "$WEBROOT/venv/bin/python3" ]; then
  echo "  ❌ venv không tồn tại: $WEBROOT/venv/bin/python3"
  exit 1
fi

cd "$WEBROOT"
nohup venv/bin/python3 -B server.py > "$LOG" 2>&1 &
NEW_PID=$!
echo "  ✓ Python started (PID: $NEW_PID)"

# 4. Health check
echo "  ► Health check..."
for i in 1 2 3 4 5 6 7 8 9 10; do
  sleep 2
  if curl -fsS "$HEALTH_URL" >/dev/null 2>&1; then
    echo "  ✓ Health OK"
    break
  fi
  if [ "$i" -eq 10 ]; then
    echo "  ⚠️  Health check failed sau 20s — xem log:"
    tail -30 "$LOG"
    exit 1
  fi
done

echo ""
echo "──────────────────────────────────────────────"
echo "  ✅ Deploy xong"
echo "──────────────────────────────────────────────"
echo "  Landing:  https://vnstock.io.vn/"
echo "  App:      https://vnstock.io.vn/app"
echo "  Log live: tail -f $LOG"
echo ""
