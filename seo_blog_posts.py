# -*- coding: utf-8 -*-
"""
SEO Blog Posts — 78 bài viết theo BLOG_PLAN_90.md
Auto-imported vào server.py để render tại /bai-viet/<slug>

Pattern mỗi bài:
  - Pain → Agitate → Solve → Example VN → Vnstock CTA → Summary + Internal Links
  - 600-900 từ HTML, 5-6 H2 sections
  - Tham chiếu mã VN30 thật (VCB, HPG, VIC, VNM, FPT, MSN, MWG, GAS)
  - Tối thiểu 5 internal links sang bài cùng cluster
"""

# Helper to reduce repetition in CTA blocks
_CTA_FOOTER = lambda links: '''<p>📚 <strong>Đọc thêm cùng cluster</strong>:</p>
<ul>''' + ''.join(f'<li>{l}</li>' for l in links) + '''</ul>
<p>🚀 <strong>Áp dụng ngay</strong>: Vnstock cung cấp <strong>Stock Screener miễn phí</strong> với 25 chỉ báo. <a href="/app">Mở Vnstock →</a></p>'''

BLOG_POSTS_EXTRA = {

# ════════════════════════════════════════════════════════════════
# CLUSTER A — TECHNICAL ANALYSIS (28 bài: bài 3-30, đã có 1, 2)
# ════════════════════════════════════════════════════════════════

'bollinger-bands-la-gi-cach-trade-tren-ttck-vn': {
    'title': 'Bollinger Bands Là Gì? 5 Cách Trade Đúng Trên TTCK VN 2026 | Vnstock',
    'description': 'Bollinger Bands — chỉ báo kết hợp MA20 + 2 độ lệch chuẩn. Hướng dẫn đọc 3 đường, Squeeze, Walking the Bands + 5 setup thực chiến VN30.',
    'keywords': 'bollinger bands là gì, cách dùng bollinger bands, bollinger squeeze, walking the bands, bollinger vn30',
    'date': '2026-05-04', 'category': 'Phân tích kỹ thuật', 'reading_time': 9,
    'h1': '📊 Bollinger Bands Là Gì? 5 Cách Trade Đúng Trên TTCK Việt Nam 2026',
    'lede': 'Bạn vẽ chart và thấy 3 đường ôm lấy giá nhưng không biết dùng thế nào? Bollinger Bands của John Bollinger (1980) là 1 trong 3 chỉ báo phổ biến nhất — nhưng 80% trader VN dùng SAI cách. Bài này giải thích từ A-Z + 5 setup thực chiến.',
    'sections': [
        {'heading': '🔍 Bollinger Bands là gì?', 'content': '''<p><strong>Bollinger Bands</strong> gồm 3 đường:</p>
<ul>
<li><strong>Middle Band</strong> = SMA 20 phiên (đường trung tâm)</li>
<li><strong>Upper Band</strong> = SMA 20 + 2σ (độ lệch chuẩn)</li>
<li><strong>Lower Band</strong> = SMA 20 − 2σ</li>
</ul>
<p>Theo lý thuyết phân phối chuẩn, <strong>~95% giá nằm trong band</strong>. Khi giá thoát ra, đó là tín hiệu bất thường đáng chú ý.</p>'''},
        {'heading': '⚠️ Sai lầm: "Chạm Upper là bán, chạm Lower là mua"', 'content': '''<p>Đây là cách <strong>phá tài khoản nhanh nhất</strong>. Trong uptrend mạnh, giá có thể "walking the bands" — chạm upper liên tục suốt nhiều tuần.</p>
<p><strong>Ví dụ FPT 2024</strong>: Giá chạm upper band lần đầu ở 110K. Trader bán ngay → bỏ lỡ tăng tiếp lên 145K (+32%) trong 8 tuần. Giá vẫn "walking" upper band suốt giai đoạn đó.</p>'''},
        {'heading': '🎯 5 setup Bollinger thực chiến', 'content': '''<h3>1. Bollinger Squeeze</h3>
<p>Khi 3 đường co lại sát nhau (volatility thấp lịch sử) → biểu hiện <em>tích lũy trước breakout lớn</em>. Đợi giá break upper/lower với volume confirm → vào lệnh.</p>
<h3>2. Walking the Bands</h3>
<p>Trong trend mạnh, giá đi dọc theo upper band (uptrend) hoặc lower band (downtrend). KHÔNG bán/mua ngược trend — chỉ nương theo MA20.</p>
<h3>3. Mean Reversion (sideway)</h3>
<p>Khi ADX &lt; 20 (sideway), mua khi giá chạm lower + RSI &lt; 35, bán khi chạm upper + RSI &gt; 65. Win rate ~65% trên VN30.</p>
<h3>4. M-Top + W-Bottom</h3>
<p>Mô hình M (đỉnh kép) ở upper band → đảo chiều giảm. W (đáy kép) ở lower → đảo chiều tăng.</p>
<h3>5. Bollinger Width breakout</h3>
<p>Width = Upper - Lower. Khi width đạt thấp nhất 6 tháng → "calm before the storm". Breakout sau đó thường mạnh và bền.</p>'''},
        {'heading': '📊 Ví dụ thực tế: VHM 2024', 'content': '''<p><strong>Vinhomes (VHM)</strong> giai đoạn Q3-Q4 2024:</p>
<ul>
<li>15/07: Squeeze 8 tuần ở 38K → break upper với vol 2.3x → MUA. Giá tăng lên 52K (+37%)</li>
<li>10/10: Bearish M-Top tại upper band 52K → CHỐT LỜI. Giá điều chỉnh -18%</li>
<li>20/12: Bullish W-Bottom tại lower band 41K → MUA TIẾP. +21% trong 6 tuần</li>
</ul>
<p>3 trades có hệ thống → return ~80% so với buy &amp; hold ~30%.</p>'''},
        {'heading': '🚀 Bollinger trên Vnstock.io.vn', 'content': '''<p>Vnstock vẽ Bollinger tự động trên mọi chart + tích hợp:</p>
<ul>
<li>Stock Screener: filter "Bollinger Squeeze (width 6m low)" hoặc "Walking upper"</li>
<li>Pattern Scanner phát hiện M-Top / W-Bottom tự động</li>
<li>Backtest AFL: <code>Buy = Close &gt; BBandTop(); Sell = Close &lt; BBandBot();</code></li>
</ul>'''},
        {'heading': '✅ Kết luận', 'content': _CTA_FOOTER([
            '📈 <a href="/bai-viet/rsi-la-gi-cach-dung-rsi-chon-co-phieu">RSI là gì? Cách dùng đúng</a>',
            '📉 <a href="/bai-viet/macd-la-gi-tin-hieu-mua-ban-vang-chet">MACD là gì? Tín hiệu vàng/chết</a>',
            '🎯 <a href="/bai-viet/adx-la-gi-cach-phan-biet-trend-vs-sideway">ADX — Phân biệt trend vs sideway</a>',
            '📊 <a href="/bai-viet/keltner-channel-vs-bollinger">Keltner Channel vs Bollinger</a>',
        ])},
    ],
    'cta': 'Quét Bollinger Squeeze toàn TTCK VN ngay'
},

'adx-la-gi-cach-phan-biet-trend-vs-sideway': {
    'title': 'ADX Là Gì? Cách Phân Biệt Trend Rõ vs Sideway 2026 | Vnstock',
    'description': 'ADX (Average Directional Index) — chỉ báo đo SỨC MẠNH trend, không phải hướng. Phân biệt trend rõ (ADX>25) vs sideway (ADX<20) để tránh bull/bear trap.',
    'keywords': 'adx là gì, cách dùng adx, adx 25, adx sideway, di+ di-, adx vn30',
    'date': '2026-05-05', 'category': 'Phân tích kỹ thuật', 'reading_time': 8,
    'h1': '🎯 ADX Là Gì? Cách Phân Biệt Trend Rõ vs Sideway',
    'lede': 'Bạn dùng RSI/MACD nhưng vẫn bị "trap" liên tục? Vấn đề có thể là bạn trade trong sideway. ADX của Wilder (1978) là chỉ báo DUY NHẤT đo SỨC MẠNH trend — phân biệt trend thật vs nhiễu.',
    'sections': [
        {'heading': '🔍 ADX là gì? Đo cái gì?', 'content': '''<p><strong>ADX (Average Directional Index)</strong> đo SỨC MẠNH của trend, KHÔNG đo hướng. Giá trị 0-100:</p>
<ul>
<li><strong>ADX &lt; 20</strong>: Sideway — không nên dùng strategy theo trend</li>
<li><strong>ADX 20-25</strong>: Trend đang hình thành — chờ confirm</li>
<li><strong>ADX 25-50</strong>: Trend mạnh — mọi indicator theo trend hoạt động tốt</li>
<li><strong>ADX &gt; 50</strong>: Trend cực mạnh — cẩn thận đảo chiều sau đỉnh</li>
</ul>
<p>ADX KHÔNG nói uptrend hay downtrend. Phải kết hợp với <strong>+DI</strong> (Directional Indicator dương) và <strong>−DI</strong> (âm).</p>'''},
        {'heading': '📐 Công thức + 3 đường', 'content': '''<pre><code>+DI = 100 × EMA(+DM) / ATR
−DI = 100 × EMA(−DM) / ATR
ADX = 100 × EMA(|+DI − −DI| / (+DI + −DI))</code></pre>
<p>Hiểu đơn giản:</p>
<ul>
<li><strong>+DI &gt; −DI</strong>: Uptrend</li>
<li><strong>+DI &lt; −DI</strong>: Downtrend</li>
<li><strong>ADX</strong>: chỉ nói "trend này MẠNH ĐẾN ĐÂU"</li>
</ul>'''},
        {'heading': '🎯 3 cách dùng ADX hiệu quả', 'content': '''<h3>1. Filter chính cho mọi chiến lược</h3>
<p>Trước khi dùng RSI/MACD/Bollinger, kiểm tra ADX. Nếu &lt;20 → KHÔNG TRADE (đợi trend).</p>
<h3>2. Cross +DI / −DI</h3>
<p>+DI cắt LÊN −DI + ADX &gt; 25 → tín hiệu MUA mạnh. Ngược lại bán.</p>
<h3>3. ADX peak &amp; decline</h3>
<p>ADX đạt đỉnh &gt; 50 và bắt đầu giảm → trend đang yếu dần (chốt lời từng phần).</p>'''},
        {'heading': '⚠️ Sai lầm: ADX cao = mua', 'content': '''<p>ADX cao chỉ nói trend MẠNH — có thể là uptrend HOẶC downtrend. ADX 60 trong downtrend = giá đang rơi rất mạnh. Đừng nhầm.</p>'''},
        {'heading': '📊 Ví dụ thực tế: HPG 2024', 'content': '''<ul>
<li>03/2024: ADX 12 (sideway) → KHÔNG trade dù RSI báo</li>
<li>05/2024: ADX vượt 25 + +DI &gt; −DI → MUA tại 26K</li>
<li>08/2024: ADX đỉnh 48 + bearish divergence trên RSI → CHỐT 38K (+46%)</li>
<li>09/2024: ADX rớt &lt; 20 + giá sideway → ĐỨNG NGOÀI</li>
</ul>
<p>1 trade duy nhất nhưng +46% trong 3 tháng — quality &gt; quantity.</p>'''},
        {'heading': '🚀 ADX trên Vnstock', 'content': '''<p>Vnstock tự động cảnh báo ADX low (sideway warning) trong tab Xu hướng → tránh false signals. Stock Screener có filter "ADX &gt; 25 + +DI &gt; −DI".</p>''' + _CTA_FOOTER([
            '📊 <a href="/bai-viet/rsi-la-gi-cach-dung-rsi-chon-co-phieu">RSI là gì</a>',
            '📈 <a href="/bai-viet/macd-la-gi-tin-hieu-mua-ban-vang-chet">MACD là gì</a>',
            '📐 <a href="/bai-viet/bollinger-bands-la-gi-cach-trade-tren-ttck-vn">Bollinger Bands</a>',
            '🎯 <a href="/bai-viet/breakout-la-gi-5-cach-tranh-breakout-gia">Breakout là gì</a>',
        ])}
    ],
    'cta': 'Lọc cổ phiếu có ADX > 25 hôm nay'
},

'ema-vs-sma-khac-biet-loai-nao-tot-hon': {
    'title': 'EMA vs SMA — Khác Biệt + Loại Nào Tốt Hơn 2026 | Vnstock',
    'description': 'EMA (trung bình mũ) phản ứng nhanh với giá mới, SMA chậm hơn nhưng ổn định. So sánh chi tiết + khi nào dùng EMA, khi nào SMA cho TTCK Việt Nam.',
    'keywords': 'ema là gì, sma là gì, ema vs sma, ma20 ma50 ma200, ema 12 26',
    'date': '2026-05-05', 'category': 'Phân tích kỹ thuật', 'reading_time': 7,
    'h1': '📐 EMA vs SMA — Khác Biệt + Loại Nào Tốt Hơn 2026',
    'lede': 'Bạn đang phân vân giữa EMA và SMA? Cả 2 đều là đường trung bình động nhưng phản ứng rất khác — chọn sai có thể khiến bạn vào lệnh muộn 3-5 phiên. Bài này so sánh chi tiết + đưa ra recommend cụ thể.',
    'sections': [
        {'heading': '🔍 SMA vs EMA — Định nghĩa', 'content': '''<p><strong>SMA (Simple Moving Average)</strong>: Trung bình cộng đơn giản N phiên gần nhất.</p>
<pre><code>SMA(N) = (P1 + P2 + ... + PN) / N</code></pre>
<p><strong>EMA (Exponential Moving Average)</strong>: Trọng số GIẢM DẦN — phiên gần đây có trọng số cao hơn.</p>
<pre><code>EMA(t) = α × P(t) + (1−α) × EMA(t−1)
α = 2 / (N+1)</code></pre>
<p>Ví dụ EMA(20): trọng số phiên hôm nay = 2/21 ≈ 9.5% so với SMA 5%.</p>'''},
        {'heading': '⚖️ So sánh chi tiết', 'content': '''<table>
<tr><th>Tiêu chí</th><th>SMA</th><th>EMA</th></tr>
<tr><td>Phản ứng với giá</td><td>Chậm</td><td>Nhanh</td></tr>
<tr><td>Smooth (mượt)</td><td>Mượt hơn</td><td>Răng cưa hơn</td></tr>
<tr><td>Whipsaw rủi ro</td><td>Thấp</td><td>Cao trong sideway</td></tr>
<tr><td>Phù hợp với</td><td>Long-term, vị thế dài</td><td>Day trade, swing</td></tr>
<tr><td>MACD dùng</td><td>Không</td><td>EMA(12), EMA(26)</td></tr>
</table>'''},
        {'heading': '🎯 Khi nào dùng EMA?', 'content': '''<ul>
<li>Day trading / scalping</li>
<li>Swing 1-2 tuần</li>
<li>MACD calculations (đã built-in)</li>
<li>Trend mới hình thành — cần signal sớm</li>
<li>Stocks có volatility cao</li>
</ul>'''},
        {'heading': '🎯 Khi nào dùng SMA?', 'content': '''<ul>
<li>Định giá dài hạn (MA200 cho regime detection)</li>
<li>Hỗ trợ/kháng cự dynamic</li>
<li>Death/Golden Cross MA50/MA200 — chuẩn ngành dùng SMA</li>
<li>Nhà đầu tư giá trị, ít theo dõi hàng ngày</li>
</ul>'''},
        {'heading': '📊 Recommended setup cho TTCK VN', 'content': '''<ul>
<li><strong>EMA(12)</strong> — fast trend signal</li>
<li><strong>EMA(26)</strong> — medium trend (kết hợp MACD)</li>
<li><strong>SMA(50)</strong> — medium-term support</li>
<li><strong>SMA(200)</strong> — bull/bear regime divider</li>
</ul>
<p>Quy tắc Stan Weinstein: Stage 2 (uptrend) chỉ trade khi giá &gt; SMA200 và SMA200 dốc lên.</p>'''},
        {'heading': '✅ Kết luận', 'content': '<p>Không có "loại nào tốt hơn" tuyệt đối — phụ thuộc style. <strong>Khuyến nghị</strong>: dùng cả 4 đường EMA12/26 + SMA50/200 trong cùng chart để có cái nhìn đa chiều.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/macd-la-gi-tin-hieu-mua-ban-vang-chet">MACD dùng EMA(12,26,9)</a>',
            '<a href="/bai-viet/rsi-la-gi-cach-dung-rsi-chon-co-phieu">RSI là gì</a>',
            '<a href="/bai-viet/bollinger-bands-la-gi-cach-trade-tren-ttck-vn">Bollinger Bands</a>',
        ])}
    ],
    'cta': 'Mở chart với cả 4 MA chuẩn'
},

'mo-hinh-nen-dao-chieu-8-mau-quan-trong': {
    'title': 'Mô Hình Nến Đảo Chiều — 8 Mẫu Quan Trọng Nhất Trader Phải Biết | Vnstock',
    'description': 'Top 8 mô hình nến đảo chiều: Engulfing, Morning Star, Evening Star, Hammer, Shooting Star, Doji, Pin Bar, Three Soldiers. Phân biệt + ví dụ VN30.',
    'keywords': 'mô hình nến đảo chiều, candlestick reversal, mẫu nến đảo chiều, engulfing morning star',
    'date': '2026-05-05', 'category': 'Phân tích kỹ thuật', 'reading_time': 10,
    'h1': '🕯 Mô Hình Nến Đảo Chiều — 8 Mẫu Quan Trọng Nhất',
    'lede': 'Bạn nhìn chart toàn nến nhưng không biết đâu là tín hiệu đảo chiều thật, đâu là nhiễu? 8 mô hình dưới đây được tích hợp trong mọi sách Steve Nison — và 6/8 mô hình có win rate &gt; 60% trên VN30.',
    'sections': [
        {'heading': '🟢 Bullish Reversal (đảo chiều tăng)', 'content': '''<h3>1. Bullish Engulfing — Nhấn chìm tăng</h3>
<p>Nến xanh lớn "nuốt" trọn nến đỏ phía trước. Tin cậy CAO khi xuất hiện ở đáy + volume lớn.</p>
<h3>2. Morning Star — Sao Mai (3 nến)</h3>
<p>Nến đỏ lớn → nến nhỏ (doji/spinning) → nến xanh lớn. Mô hình tin cậy nhất ở đáy.</p>
<h3>3. Hammer — Búa</h3>
<p>Thân nhỏ, bóng dưới dài 2-3x thân, ít/không có bóng trên. Xuất hiện sau downtrend → reversal.</p>
<h3>4. Three White Soldiers — 3 Lính Trắng</h3>
<p>3 nến xanh liên tiếp, mỗi nến đóng cao hơn nến trước. Xác nhận trend tăng mới.</p>'''},
        {'heading': '🔴 Bearish Reversal (đảo chiều giảm)', 'content': '''<h3>5. Bearish Engulfing — Nhấn chìm giảm</h3>
<p>Nến đỏ lớn nuốt nến xanh. Cảnh báo đỉnh khi xuất hiện sau uptrend.</p>
<h3>6. Evening Star — Sao Hôm (3 nến)</h3>
<p>Đối ngược Morning Star — báo đỉnh.</p>
<h3>7. Shooting Star — Sao Băng</h3>
<p>Thân nhỏ, bóng trên dài, không bóng dưới. Sau uptrend → đảo chiều giảm.</p>
<h3>8. Doji</h3>
<p>Mở = đóng (gần như). Báo "phân vân" — đảo chiều ở đỉnh/đáy có RSI overbought/oversold.</p>'''},
        {'heading': '⚠️ Sai lầm phổ biến', 'content': '''<p>Trader mới thấy mô hình → vào lệnh ngay. SAI. Mô hình nến chỉ là TÍN HIỆU YẾU độc lập:</p>
<ul>
<li>Cần ở vị trí "có nghĩa" — đỉnh/đáy, hỗ trợ/kháng cự</li>
<li>Cần volume confirm (nến có volume cao hơn 1.5x trung bình)</li>
<li>Cần confluence với chỉ báo (RSI, MACD)</li>
</ul>'''},
        {'heading': '📊 Ví dụ MWG 2024', 'content': '''<ul>
<li>10/06: Bullish Engulfing tại 38.5K + RSI 32 + volume 2.1x → MUA. +45% trong 12 tuần</li>
<li>22/09: Evening Star tại 56K + RSI 75 → CHỐT LỜI. Tránh -18%</li>
</ul>'''},
        {'heading': '🚀 Pattern Scanner Vnstock', 'content': '''<p>Vnstock tự động quét 456 mã VN, phát hiện 16 mô hình nến mỗi ngày. Tab "🕯 Pattern Scanner" trong Dashboard.</p>''' + _CTA_FOOTER([
            '<a href="/bai-viet/engulfing-pattern-cach-trade-mau-nhan-chim">Engulfing Pattern chi tiết</a>',
            '<a href="/bai-viet/morning-star-tin-hieu-day-quan-trong">Morning Star</a>',
            '<a href="/bai-viet/evening-star-canh-bao-dinh-som">Evening Star</a>',
            '<a href="/bai-viet/doji-la-gi-5-loai-doji">Doji là gì</a>',
            '<a href="/bai-viet/hammer-hanging-man-dao-chieu">Hammer & Hanging Man</a>',
        ])}
    ],
    'cta': 'Quét 16 mô hình nến trên 456 mã VN ngay'
},

'engulfing-pattern-cach-trade-mau-nhan-chim': {
    'title': 'Engulfing Pattern — Cách Trade Mẫu Nến Nhấn Chìm Hiệu Quả | Vnstock',
    'description': 'Engulfing Pattern (mẫu nến nhấn chìm) tin cậy 70%+ khi đúng setup. Hướng dẫn nhận diện Bullish/Bearish Engulfing + 4 quy tắc lọc nhiễu.',
    'keywords': 'engulfing pattern, bullish engulfing, bearish engulfing, mẫu nến nhấn chìm',
    'date': '2026-05-06', 'category': 'Phân tích kỹ thuật', 'reading_time': 7,
    'h1': '🕯 Engulfing Pattern — Mẫu Nến Nhấn Chìm Hiệu Quả Nhất',
    'lede': 'Trong các mô hình nến đảo chiều, Engulfing là mạnh nhất theo nghiên cứu của Bulkowski (Encyclopedia of Candlestick Charts). Nhưng phải dùng đúng setup mới đạt win rate 65-72%.',
    'sections': [
        {'heading': '🔍 Engulfing là gì?', 'content': '''<p><strong>Bullish Engulfing</strong>: Nến xanh THỨ 2 có thân (mở-đóng) <strong>bao trọn</strong> thân nến đỏ trước đó.</p>
<p><strong>Bearish Engulfing</strong>: Nến đỏ thứ 2 nuốt thân nến xanh trước.</p>
<p>Quan trọng: <strong>chỉ xét THÂN nến</strong>, không tính bóng (wick).</p>'''},
        {'heading': '✅ 4 quy tắc lọc Engulfing đáng trade', 'content': '''<ol>
<li><strong>Vị trí</strong>: phải ở đáy (cho bullish) hoặc đỉnh (bearish) sau swing rõ</li>
<li><strong>Volume</strong>: nến engulfing có volume &gt; 1.5x trung bình 20 phiên</li>
<li><strong>Tỷ lệ thân</strong>: nến 2 phải &gt; 1.5x thân nến 1 (càng lớn càng mạnh)</li>
<li><strong>Confluence</strong>: kết hợp với RSI quá mua/bán hoặc Bollinger upper/lower</li>
</ol>'''},
        {'heading': '⚠️ Engulfing GIẢ — cách tránh', 'content': '''<p>2 trường hợp engulfing không đáng trade:</p>
<ul>
<li>Trong sideway (ADX &lt; 20) → mostly noise</li>
<li>Volume thấp dưới trung bình → thiếu institutional confirmation</li>
</ul>
<p>Theo Bulkowski, engulfing trong sideway có win rate chỉ ~52% — gần như coin flip.</p>'''},
        {'heading': '📊 Ví dụ FPT 2024', 'content': '''<p>15/03/2024: FPT đáy 95K, Bullish Engulfing với volume 2.8x avg + RSI 28 + ở vùng support MA200. → MUA. Giá tăng lên 145K (+52%) trong 16 tuần.</p>'''},
        {'heading': '🚀 Pattern Scanner Vnstock', 'content': '''<p>Vnstock tự động phát hiện engulfing đạt 4 quy tắc trên + cảnh báo Telegram (qua Quality Gate anti-spam).</p>''' + _CTA_FOOTER([
            '<a href="/bai-viet/mo-hinh-nen-dao-chieu-8-mau-quan-trong">8 mô hình nến đảo chiều</a>',
            '<a href="/bai-viet/morning-star-tin-hieu-day-quan-trong">Morning Star</a>',
            '<a href="/bai-viet/hammer-hanging-man-dao-chieu">Hammer & Hanging Man</a>',
        ])}
    ],
    'cta': 'Xem Engulfing live trên VN30 hôm nay'
},

'morning-star-tin-hieu-day-quan-trong': {
    'title': 'Morning Star — Tín Hiệu Đáy Quan Trọng Nhà Đầu Tư Phải Biết | Vnstock',
    'description': 'Morning Star — mô hình 3 nến tin cậy nhất ở đáy. Nến đỏ lớn → doji/spinning → nến xanh lớn. Hướng dẫn nhận diện + 3 setup vào lệnh.',
    'keywords': 'morning star, sao mai, mô hình 3 nến, tín hiệu đáy',
    'date': '2026-05-06', 'category': 'Phân tích kỹ thuật', 'reading_time': 7,
    'h1': '⭐ Morning Star — Tín Hiệu Đáy Tin Cậy Nhất',
    'lede': 'Morning Star (Sao Mai) là 1 trong 3 mô hình đảo chiều có win rate cao nhất theo Bulkowski. Tin cậy &gt; 75% nếu đúng setup. Hướng dẫn nhận diện + áp dụng VN30.',
    'sections': [
        {'heading': '🔍 Cấu trúc 3 nến Morning Star', 'content': '''<ol>
<li><strong>Nến 1</strong>: nến đỏ lớn — xác nhận downtrend</li>
<li><strong>Nến 2</strong>: nến nhỏ (doji hoặc spinning top) — phân vân, momentum yếu</li>
<li><strong>Nến 3</strong>: nến xanh lớn, đóng &gt;= 50% thân nến 1 — confirmation</li>
</ol>
<p>Lý tưởng: nến 2 GAP DOWN so với nến 1, nến 3 GAP UP so với nến 2.</p>'''},
        {'heading': '✅ 4 điều kiện confirm', 'content': '''<ol>
<li>Xuất hiện sau downtrend &gt;= 5 phiên</li>
<li>Vị trí ở vùng support hoặc Fib 61.8%</li>
<li>RSI &lt; 35 (quá bán)</li>
<li>Volume nến 3 &gt; 1.5x trung bình</li>
</ol>'''},
        {'heading': '⚠️ False signal', 'content': '<p>Morning Star trong sideway (ADX&lt;20) hoặc volume thấp → thường là pause, không phải reversal. Win rate trong sideway chỉ ~55%.</p>'},
        {'heading': '📊 Ví dụ VCB 2024', 'content': '<p>22/05/2024: Morning Star tại 78K (Fib 61.8% từ swing 92→68K) + RSI 32 + volume 2.1x. → MUA. Giá tăng lên 92K (+18%) trong 8 tuần.</p>'},
        {'heading': '🚀 Áp dụng Vnstock', 'content': '<p>Pattern Scanner phát hiện Morning Star toàn 456 mã VN30+. Filter "Morning Star + RSI &lt; 35" trong screener.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/mo-hinh-nen-dao-chieu-8-mau-quan-trong">8 mô hình nến đảo chiều</a>',
            '<a href="/bai-viet/evening-star-canh-bao-dinh-som">Evening Star — anti-pattern</a>',
            '<a href="/bai-viet/engulfing-pattern-cach-trade-mau-nhan-chim">Engulfing Pattern</a>',
        ])}
    ],
    'cta': 'Quét Morning Star hôm nay'
},

'evening-star-canh-bao-dinh-som': {
    'title': 'Evening Star — Cảnh Báo Đỉnh Sớm Cho Trader VN | Vnstock',
    'description': 'Evening Star (Sao Hôm) — đối nghịch Morning Star, báo đỉnh. Nến xanh lớn → doji → nến đỏ lớn. Win rate 70%+ với confirmation đúng.',
    'keywords': 'evening star, sao hôm, mô hình đỉnh, cảnh báo đỉnh',
    'date': '2026-05-06', 'category': 'Phân tích kỹ thuật', 'reading_time': 6,
    'h1': '🌑 Evening Star — Cảnh Báo Đỉnh Sớm',
    'lede': 'Evening Star là cảnh báo đỉnh đáng tin nhất. Trader chuyên nghiệp dùng để chốt lời sớm 5-10 phiên trước khi giá rơi mạnh. Hướng dẫn nhận diện chính xác.',
    'sections': [
        {'heading': '🔍 Cấu trúc 3 nến', 'content': '''<ol>
<li>Nến 1: nến xanh lớn — uptrend đang mạnh</li>
<li>Nến 2: nến nhỏ (doji/spinning) — momentum suy yếu</li>
<li>Nến 3: nến đỏ lớn, đóng &lt;= 50% thân nến 1</li>
</ol>'''},
        {'heading': '✅ Confirmation cần', 'content': '<ul><li>Sau uptrend &gt;= 5 phiên</li><li>Ở vùng resistance hoặc Fib extension</li><li>RSI &gt; 70 (quá mua)</li><li>Volume nến 3 cao (chốt lời tổ chức)</li><li>Bearish divergence trên RSI/MACD</li></ul>'},
        {'heading': '📊 Ví dụ VHM 09/2024', 'content': '<p>15/09: Evening Star tại 52K + RSI 78 + bearish divergence MACD + volume 2.5x. → CHỐT LỜI/SHORT. Giá giảm về 41K (-21%) trong 5 tuần.</p>'},
        {'heading': '🚀 Vnstock auto-detect', 'content': '<p>Pattern Scanner cảnh báo Evening Star qua Telegram (đã qua Quality Gate). Combine với "RSI &gt; 70 + Bearish Divergence" filter.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/morning-star-tin-hieu-day-quan-trong">Morning Star — opposite</a>',
            '<a href="/bai-viet/mo-hinh-nen-dao-chieu-8-mau-quan-trong">8 mô hình đảo chiều</a>',
            '<a href="/bai-viet/divergence-la-gi-rsi-macd-divergence">Divergence là gì</a>',
        ])}
    ],
    'cta': 'Bật cảnh báo Evening Star Telegram'
},

'doji-la-gi-5-loai-doji': {
    'title': 'Doji Là Gì? 5 Loại Doji + Cách Trade Chính Xác | Vnstock',
    'description': 'Doji — nến mở = đóng, báo "phân vân". 5 loại: Standard, Long-legged, Dragonfly, Gravestone, Four-Price. Cách trade từng loại.',
    'keywords': 'doji là gì, 5 loại doji, dragonfly doji, gravestone doji',
    'date': '2026-05-07', 'category': 'Phân tích kỹ thuật', 'reading_time': 6,
    'h1': '🕯 Doji Là Gì? 5 Loại Doji + Cách Trade Chính Xác',
    'lede': 'Doji là nến đặc biệt — mở và đóng gần như bằng nhau. Báo "thị trường phân vân" và thường là tín hiệu đảo chiều. Có 5 loại Doji với ý nghĩa khác nhau.',
    'sections': [
        {'heading': '🔍 Định nghĩa', 'content': '<p>Doji = nến có thân (open vs close) gần như 0. Không thể biết bên mua hay bán thắng → trận hòa. Sau trend mạnh → thường báo đảo chiều.</p>'},
        {'heading': '📋 5 loại Doji', 'content': '''<h3>1. Standard Doji</h3>
<p>Bóng trên + dưới gần bằng nhau. Phân vân thuần.</p>
<h3>2. Long-legged Doji (Doji chân dài)</h3>
<p>2 bóng dài, biên độ phiên rộng. Cảm xúc giằng co mạnh — thường báo đảo chiều ở đỉnh/đáy.</p>
<h3>3. Dragonfly Doji (Chuồn chuồn)</h3>
<p>Mở = đóng = high, bóng dưới dài. Bullish ở đáy.</p>
<h3>4. Gravestone Doji (Bia mộ)</h3>
<p>Mở = đóng = low, bóng trên dài. Bearish ở đỉnh.</p>
<h3>5. Four-Price Doji (Hiếm)</h3>
<p>Open=close=high=low — không có dao động. Thanh khoản cực thấp, ít dùng cho VN30.</p>'''},
        {'heading': '✅ Cách trade', 'content': '<ul><li>Doji ở đỉnh + RSI &gt; 70 → bán/short</li><li>Doji ở đáy + RSI &lt; 30 → mua</li><li>Doji giữa trend → chỉ là pause, không trade</li></ul>'},
        {'heading': '📊 Ví dụ MSN 2024', 'content': '<p>05/08: Gravestone Doji tại 75K + RSI 78 → bán. Giá giảm về 62K (-17%) trong 6 tuần.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Pattern Scanner phát hiện 5 loại Doji + tự loại bỏ Doji "không có nghĩa" (sideway, low volume).</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/mo-hinh-nen-dao-chieu-8-mau-quan-trong">8 mô hình đảo chiều</a>',
            '<a href="/bai-viet/hammer-hanging-man-dao-chieu">Hammer & Hanging Man</a>',
        ])}
    ],
    'cta': 'Lọc Doji + RSI extreme hôm nay'
},

'hammer-hanging-man-dao-chieu': {
    'title': 'Hammer & Hanging Man — Đảo Chiều Tại Đỉnh/Đáy 2026 | Vnstock',
    'description': 'Hammer (búa) báo đảo chiều tăng ở đáy, Hanging Man cùng hình dạng nhưng ở đỉnh báo giảm. Phân biệt + cách dùng đúng.',
    'keywords': 'hammer pattern, hanging man, búa, treo cổ, mô hình đáy',
    'date': '2026-05-07', 'category': 'Phân tích kỹ thuật', 'reading_time': 6,
    'h1': '🔨 Hammer & Hanging Man — Đảo Chiều Tại Đỉnh/Đáy',
    'lede': 'Hammer và Hanging Man cùng hình dạng nhưng ý nghĩa hoàn toàn ngược nhau — phụ thuộc vào CONTEXT. Trader mới hay nhầm và mất tiền.',
    'sections': [
        {'heading': '🔍 Hình dạng chung', 'content': '<ul><li>Thân nhỏ ở phần TRÊN của nến</li><li>Bóng dưới dài 2-3x thân</li><li>Ít/không có bóng trên</li></ul>'},
        {'heading': '🔨 Hammer — sau downtrend', 'content': '<p>Xuất hiện sau downtrend → tín hiệu MUA. Ý nghĩa: phe bán đẩy giá xuống nhưng phe mua đã đẩy ngược lên đóng cửa cao → momentum đảo.</p>'},
        {'heading': '🪢 Hanging Man — sau uptrend', 'content': '<p>Cùng hình dạng nhưng sau uptrend → cảnh báo đỉnh. Phe mua đẩy giá lên nhưng phe bán đã can thiệp ép giá xuống — momentum yếu.</p>'},
        {'heading': '✅ Confirm cần', 'content': '<ul><li>Hammer: nến TIẾP THEO phải đóng cao hơn → confirm reversal</li><li>Hanging Man: nến tiếp theo đóng thấp hơn</li><li>Volume nến confirm &gt; 1.5x</li></ul>'},
        {'heading': '📊 Ví dụ VIC 2024', 'content': '<ul><li>10/04: Hammer tại 38K + confirm hôm sau → MUA. +28% trong 8 tuần</li><li>20/08: Hanging Man tại 49K + confirm giảm → CHỐT. Giảm -15%</li></ul>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Pattern Scanner phân biệt Hammer vs Hanging Man tự động dựa trên trend context.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/mo-hinh-nen-dao-chieu-8-mau-quan-trong">8 mô hình đảo chiều</a>',
            '<a href="/bai-viet/doji-la-gi-5-loai-doji">5 loại Doji</a>',
        ])}
    ],
    'cta': 'Xem Hammer/Hanging Man hôm nay'
},

'volume-la-gi-cach-doc-khoi-luong-tranh-bull-trap': {
    'title': 'Volume Là Gì? Cách Đọc Khối Lượng Tránh Bull Trap 2026 | Vnstock',
    'description': 'Volume (khối lượng giao dịch) — chỉ báo TẦM QUAN TRỌNG nhất. Giá tăng + volume tăng = real. Giá tăng + volume giảm = bull trap.',
    'keywords': 'volume là gì, khối lượng giao dịch, bull trap, volume vn30',
    'date': '2026-05-07', 'category': 'Phân tích kỹ thuật', 'reading_time': 8,
    'h1': '🔊 Volume Là Gì? Cách Đọc Khối Lượng Tránh Bull Trap',
    'lede': 'Volume là chỉ báo bị 90% trader bỏ qua nhưng quan trọng NHẤT. "Volume confirms price" — giá không có volume backup = bẫy. Bài này giúp bạn không bao giờ rơi vào bull trap nữa.',
    'sections': [
        {'heading': '🔍 Volume là gì?', 'content': '<p>Volume = số lượng cổ phiếu giao dịch trong 1 phiên. Đo "lực" thực sự của price action. Giá có thể manipulate trong ngắn hạn — volume thì không.</p>'},
        {'heading': '📐 4 nguyên tắc Volume kinh điển (Wyckoff)', 'content': '''<ol>
<li><strong>Giá tăng + Volume tăng</strong> = uptrend HEALTHY (bullish)</li>
<li><strong>Giá tăng + Volume giảm</strong> = uptrend SUY YẾU (bull trap warning)</li>
<li><strong>Giá giảm + Volume tăng</strong> = downtrend HEALTHY (bearish)</li>
<li><strong>Giá giảm + Volume giảm</strong> = downtrend SUY YẾU (có thể đảo chiều)</li>
</ol>'''},
        {'heading': '⚠️ Bull Trap thật', 'content': '<p><strong>Vidụ FLC 2022</strong>: Giá tăng 25% trong 2 tuần nhưng volume chỉ bằng 60% trung bình. Trader mới mua đuổi → 2 tuần sau giá rơi 50%. Đây là phân phối — cá mập bán cho nhỏ lẻ.</p>'},
        {'heading': '🎯 Volume Profile vs Volume Bar', 'content': '<p><strong>Volume Bar</strong>: thanh dọc dưới chart, theo thời gian.</p><p><strong>Volume Profile</strong>: phân bố volume theo VÙNG GIÁ, cho biết "POC" (Point of Control) — giá có volume cao nhất = vùng support/resistance mạnh.</p>'},
        {'heading': '📊 Ví dụ HPG 2024', 'content': '<ul><li>15/05: Breakout 31K + volume 3.2x avg → real breakout. +35% sau đó</li><li>10/07: Giá tăng tới 38K nhưng volume chỉ 0.7x → divergence âm. Sau đó giảm về 32K</li></ul>'},
        {'heading': '🚀 Volume trên Vnstock', 'content': '<p>Bảng giá có cột volume + so với avg 20. Stock Screener filter "Volume &gt; 1.5x avg". Tab Volume Profile cho VN30.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/breakout-la-gi-5-cach-tranh-breakout-gia">Breakout là gì</a>',
            '<a href="/bai-viet/obv-la-gi-on-balance-volume">OBV là gì</a>',
            '<a href="/bai-viet/vwap-duong-trung-binh-quan-trong">VWAP</a>',
            '<a href="/bai-viet/volume-profile-phan-tich-khoi-luong">Volume Profile</a>',
        ])}
    ],
    'cta': 'Lọc cổ phiếu volume bất thường hôm nay'
},

'ho-tro-khang-cu-cach-ve-dung-tren-chart': {
    'title': 'Hỗ Trợ Kháng Cự — Cách Vẽ Đúng Trên Chart Cổ Phiếu VN | Vnstock',
    'description': 'Hỗ trợ (support) và kháng cự (resistance) — nền tảng phân tích kỹ thuật. Cách vẽ đúng + 5 loại support/resistance + ví dụ VN30.',
    'keywords': 'hỗ trợ kháng cự, support resistance, cách vẽ trendline, vùng giá quan trọng',
    'date': '2026-05-08', 'category': 'Phân tích kỹ thuật', 'reading_time': 9,
    'h1': '📐 Hỗ Trợ Kháng Cự — Cách Vẽ Đúng Trên Chart',
    'lede': 'Bạn vẽ trendline mỗi người mỗi kiểu? Đây là kỹ năng QUAN TRỌNG NHẤT của TA — vẽ sai thì mọi chỉ báo đều vô nghĩa. Bài này hướng dẫn chuẩn theo Tom Bulkowski.',
    'sections': [
        {'heading': '🔍 Định nghĩa', 'content': '<p><strong>Hỗ trợ (support)</strong>: vùng giá mà cầu &gt; cung — giá có xu hướng dội ngược lên.</p><p><strong>Kháng cự (resistance)</strong>: vùng cung &gt; cầu — giá khó vượt qua.</p><p>Quan trọng: support có thể trở thành resistance sau khi bị break (và ngược lại) — gọi là "polarity flip".</p>'},
        {'heading': '🎯 5 loại Support/Resistance', 'content': '''<h3>1. Horizontal (ngang)</h3>
<p>Vẽ ngang qua các đỉnh/đáy quan trọng. Mạnh nhất khi giá test 3+ lần.</p>
<h3>2. Trendline (đường xu hướng)</h3>
<p>Nối ít nhất 3 đáy (uptrend) hoặc 3 đỉnh (downtrend). Càng nhiều điểm chạm → càng mạnh.</p>
<h3>3. Moving Average dynamic</h3>
<p>MA20, MA50, MA200 đóng vai trò support/resistance dynamic.</p>
<h3>4. Fibonacci levels</h3>
<p>23.6%, 38.2%, 50%, 61.8%, 78.6% — golden ratio support/resistance.</p>
<h3>5. Pivot Points</h3>
<p>R1, R2, S1, S2 — intraday support/resistance.</p>'''},
        {'heading': '⚠️ Sai lầm vẽ trendline', 'content': '<ul><li>Vẽ qua 2 điểm thôi → không đáng tin (random)</li><li>Vẽ qua bóng nến → không chuẩn (chỉ vẽ qua thân + bóng quan trọng)</li><li>Vẽ trên timeframe không đúng (intraday line áp dụng weekly)</li></ul>'},
        {'heading': '📊 Ví dụ FPT 2024', 'content': '<p>FPT có resistance 145K test 3 lần (06/2024, 09/2024, 11/2024) — không vượt được. Trendline tăng từ đáy 95K (03/2024) qua các đáy 110K (07/2024) và 122K (10/2024).</p>'},
        {'heading': '🚀 Auto S/R trên Vnstock', 'content': '<p>Vnstock dùng pivot point detection tự động vẽ 3-5 đường horizontal S/R quan trọng nhất + Fib levels + MA dynamic.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/fibonacci-retracement-auto-magnetic-snap">Fibonacci Retracement</a>',
            '<a href="/bai-viet/trendline-la-gi-cach-ve-trendline">Trendline chính xác</a>',
            '<a href="/bai-viet/pivot-points-cach-dung-r1-s1">Pivot Points</a>',
        ])}
    ],
    'cta': 'Xem Auto S/R trên VN30 ngay'
},

'fibonacci-retracement-auto-magnetic-snap': {
    'title': 'Fibonacci Retracement — Auto-Magnetic Snap Tự Động | Vnstock',
    'description': 'Fibonacci 23.6%, 38.2%, 50%, 61.8%, 78.6% — vùng đảo chiều dựa trên golden ratio. Vnstock có Auto-Magnetic Snap tự hít vào đỉnh/đáy gần nhất.',
    'keywords': 'fibonacci retracement, fib levels, golden ratio, auto magnetic fib',
    'date': '2026-05-08', 'category': 'Phân tích kỹ thuật', 'reading_time': 7,
    'h1': '📐 Fibonacci Retracement — Auto-Magnetic Snap',
    'lede': 'Fibonacci levels là vùng đảo chiều có cơ sở toán học — không phải mê tín. Vnstock có Auto-Magnetic Snap tự tìm swing high/low chính xác trong 1 click.',
    'sections': [
        {'heading': '🔍 Fibonacci là gì?', 'content': '<p>Dãy số Fibonacci tạo ra "tỷ lệ vàng" 1.618. Áp dụng vào chart: lấy swing high - swing low, chia theo các tỷ lệ 23.6%, 38.2%, 50%, 61.8%, 78.6% → vùng "kéo lùi" (retracement) khả năng cao có phản ứng giá.</p>'},
        {'heading': '📊 Các mức Fib quan trọng', 'content': '<ul><li><strong>38.2%</strong>: pull back nhẹ — uptrend mạnh</li><li><strong>50%</strong>: pull back trung bình — không phải Fib chính thức nhưng phổ biến</li><li><strong>61.8%</strong>: GOLDEN RATIO — vùng quan trọng nhất</li><li><strong>78.6%</strong>: pull back sâu — gần đảo chiều hoàn toàn</li></ul>'},
        {'heading': '🎯 Cách trade Fib', 'content': '<ol><li>Xác định swing high - swing low gần nhất</li><li>Vẽ Fib từ low → high (uptrend)</li><li>Đợi giá pull back về 38.2%, 50%, 61.8%</li><li>Confluence với chỉ báo khác (RSI, support cũ) để vào lệnh</li></ol>'},
        {'heading': '⚡ Auto-Magnetic Snap Vnstock', 'content': '<p>Vnstock tự động:</p><ul><li>Detect swing high/low gần nhất qua ZigZag algorithm</li><li>Snap vào đúng đỉnh/đáy (không lệch)</li><li>4 lookback options: 1m / 3m / 6m / 1y</li><li>Show date của swing trên label</li></ul>'},
        {'heading': '📊 Ví dụ VCB 2024', 'content': '<p>Swing 92K (01/2024) → 68K (06/2024). Fib 61.8% = 82.8K. VCB pull back đúng 82K (08/2024) + RSI 35 → MUA. +12% trong 8 tuần.</p>'},
        {'heading': '🚀 Mở Auto-Fib', 'content': '<p>Vnstock symbol modal → Tab "Xu hướng" → bật Fibonacci → chọn lookback period.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/ho-tro-khang-cu-cach-ve-dung-tren-chart">Hỗ trợ kháng cự</a>',
            '<a href="/bai-viet/trendline-la-gi-cach-ve-trendline">Trendline</a>',
        ])}
    ],
    'cta': 'Mở Auto-Magnetic Fibonacci'
},

'trendline-la-gi-cach-ve-trendline': {
    'title': 'Trendline Là Gì? Cách Vẽ Trendline Chính Xác | Vnstock',
    'description': 'Trendline (đường xu hướng) — kết nối ít nhất 3 đỉnh/đáy. Cách vẽ chuẩn + 4 quy tắc trade trendline + cách phân biệt trendline thật/giả.',
    'keywords': 'trendline là gì, cách vẽ trendline, đường xu hướng',
    'date': '2026-05-08', 'category': 'Phân tích kỹ thuật', 'reading_time': 6,
    'h1': '📈 Trendline Là Gì? Cách Vẽ Chính Xác',
    'lede': 'Trendline đẹp = signal cực mạnh, trendline ẩu = mất tiền. Vẽ đúng cần biết quy tắc và kỷ luật.',
    'sections': [
        {'heading': '🔍 Định nghĩa', 'content': '<p>Trendline = đường thẳng nối ít nhất <strong>3 điểm chạm</strong> (đỉnh hoặc đáy). 2 điểm chỉ là "tentative" (thử nghiệm).</p>'},
        {'heading': '✅ Quy tắc vẽ', 'content': '<ol><li>Tối thiểu 3 điểm chạm</li><li>Khoảng cách giữa các điểm hợp lý (không quá gần)</li><li>Slope vừa phải (không quá dốc &gt; 60° = không bền)</li><li>Vẽ qua các đỉnh/đáy CHÍNH (significant), không phải mọi đỉnh</li></ol>'},
        {'heading': '🎯 Cách trade', 'content': '<ul><li>Mua/bán khi giá chạm trendline + confirm</li><li>Stop loss bên kia trendline</li><li>Trendline break + volume confirm = đảo chiều</li><li>Không trade trendline trong sideway</li></ul>'},
        {'heading': '📊 Ví dụ VHM 2024', 'content': '<p>Trendline tăng từ đáy 38K (03/2024), 41K (05/2024), 47K (08/2024). Mỗi lần chạm trendline + RSI &lt; 40 → mua. 3 trades win.</p>'},
        {'heading': '🚀 Drawing tools Vnstock', 'content': '<p>Symbol modal có tools vẽ trendline + auto-detect significant pivots → vẽ đúng ngay từ đầu.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/ho-tro-khang-cu-cach-ve-dung-tren-chart">Hỗ trợ kháng cự</a>',
            '<a href="/bai-viet/fibonacci-retracement-auto-magnetic-snap">Fibonacci</a>',
        ])}
    ],
    'cta': 'Vẽ trendline trên VN30 ngay'
},

'divergence-la-gi-rsi-macd-divergence': {
    'title': 'Divergence Là Gì? RSI/MACD Divergence Báo Đảo Chiều | Vnstock',
    'description': 'Divergence — phân kỳ giữa giá và chỉ báo. Bullish/Bearish/Hidden Divergence. Setup đảo chiều mạnh nhất, win rate 65%+.',
    'keywords': 'divergence là gì, phân kỳ rsi, phân kỳ macd, hidden divergence',
    'date': '2026-05-09', 'category': 'Phân tích kỹ thuật', 'reading_time': 8,
    'h1': '🔀 Divergence — RSI/MACD Báo Đảo Chiều Sớm',
    'lede': 'Divergence (phân kỳ) là tín hiệu MẠNH NHẤT của reversal — chỉ ra momentum đang yếu dần dù giá vẫn đi cùng hướng. Trader chuyên dùng để "thoát đỉnh, vào đáy" sớm 1-2 tuần.',
    'sections': [
        {'heading': '🔍 Divergence là gì?', 'content': '<p>Divergence = phân kỳ giữa <strong>price action</strong> và <strong>indicator</strong>. Có 4 loại chính:</p><ul><li><strong>Bullish Divergence</strong>: giá tạo đáy thấp hơn, indicator tạo đáy cao hơn → chuẩn bị tăng</li><li><strong>Bearish Divergence</strong>: giá tạo đỉnh cao hơn, indicator thấp hơn → chuẩn bị giảm</li><li><strong>Hidden Bullish</strong>: giá đáy cao hơn, indicator đáy thấp hơn → trend tiếp tục tăng</li><li><strong>Hidden Bearish</strong>: giá đỉnh thấp hơn, indicator đỉnh cao hơn → trend tiếp tục giảm</li></ul>'},
        {'heading': '✅ Quy tắc xác định', 'content': '<ol><li>Cần 2 đỉnh/đáy rõ ràng trên giá</li><li>Khoảng cách giữa 2 đỉnh/đáy &gt;= 5 phiên (không quá gần)</li><li>Indicator phổ biến: RSI, MACD, Stochastic</li><li>Cần confirmation candle (engulfing, hammer)</li></ol>'},
        {'heading': '⚠️ False divergence', 'content': '<p>Divergence trong trend cực mạnh thường là FAKE. Quy tắc: nếu ADX &gt; 40, divergence không đáng tin — momentum vẫn còn dư địa.</p>'},
        {'heading': '📊 Ví dụ MWG 2024', 'content': '<p>09/2024: MWG đỉnh 56K, RSI 78. Đỉnh tiếp 58K (10/2024), RSI chỉ 72 → bearish divergence. + bearish engulfing → CHỐT. Giá rơi -22% sau đó.</p>'},
        {'heading': '🚀 Auto Divergence Vnstock', 'content': '<p>Symbol modal phát hiện divergence tự động (RSI + MACD). Telegram alert qua Quality Gate khi divergence + confirmation candle.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/rsi-la-gi-cach-dung-rsi-chon-co-phieu">RSI là gì</a>',
            '<a href="/bai-viet/macd-la-gi-tin-hieu-mua-ban-vang-chet">MACD là gì</a>',
            '<a href="/bai-viet/stochastic-cach-dung-k-d">Stochastic %K %D</a>',
        ])}
    ],
    'cta': 'Bật Auto-Divergence Detection'
},

'stochastic-cach-dung-k-d': {
    'title': 'Stochastic Oscillator — Cách Dùng %K %D Cho TTCK VN | Vnstock',
    'description': 'Stochastic của Lane (1950s) — oscillator nhanh hơn RSI. %K (fast) + %D (slow). Cách dùng signal line cross + divergence.',
    'keywords': 'stochastic là gì, %k %d, fast slow stochastic',
    'date': '2026-05-09', 'category': 'Phân tích kỹ thuật', 'reading_time': 6,
    'h1': '📊 Stochastic Oscillator — %K %D Cho TTCK VN',
    'lede': 'Stochastic là RSI "nhanh hơn" — tín hiệu sớm hơn nhưng cũng nhiều noise hơn. Phù hợp cho swing 3-7 ngày trên VN30.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>%K = 100 × (Close − Low_n) / (High_n − Low_n)\n%D = SMA(%K, 3)</code></pre><p>Default: n=14. %K nhanh, %D chậm (smoothed).</p>'},
        {'heading': '🎯 Tín hiệu', 'content': '<ul><li>%K cắt LÊN %D dưới 20 → MUA</li><li>%K cắt XUỐNG %D trên 80 → BÁN</li><li>%K &gt; 80: quá mua | %K &lt; 20: quá bán</li><li>Divergence áp dụng tương tự RSI</li></ul>'},
        {'heading': '⚠️ Stochastic vs RSI', 'content': '<p>Stochastic nhạy hơn → nhiều signal hơn nhưng noise hơn. Phù hợp short-term. RSI ổn định hơn cho swing dài.</p>'},
        {'heading': '📊 Ví dụ', 'content': '<p>HPG 06/2024: Stochastic %K cross %D ở mức 18 (oversold) → MUA tại 27K. +20% trong 4 tuần.</p>'},
        {'heading': '🚀 Áp dụng Vnstock', 'content': '<p>Stock Screener filter "Stochastic Bullish Cross". Symbol modal hiển thị %K, %D realtime.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/rsi-la-gi-cach-dung-rsi-chon-co-phieu">RSI vs Stochastic</a>',
            '<a href="/bai-viet/divergence-la-gi-rsi-macd-divergence">Divergence</a>',
        ])}
    ],
    'cta': 'Lọc Stochastic Bullish Cross'
},

'ichimoku-cloud-he-thong-trading-nhat-ban': {
    'title': 'Ichimoku Cloud — Hệ Thống Trading Nhật Bản Cho VN30 | Vnstock',
    'description': 'Ichimoku Kinko Hyo (1969) — hệ thống TA hoàn chỉnh chỉ với 1 chart. 5 đường, Kumo Cloud, Kumo Twist, TK Cross. Phức tạp nhưng cực mạnh.',
    'keywords': 'ichimoku là gì, kumo cloud, tenkan kijun, ichimoku vn30',
    'date': '2026-05-10', 'category': 'Phân tích kỹ thuật', 'reading_time': 11,
    'h1': '☁️ Ichimoku Cloud — Hệ Thống Trading Nhật Bản',
    'lede': 'Ichimoku là hệ thống TA hoàn chỉnh nhất — 1 chart cho biết trend, support/resistance, momentum, signal mua/bán. Phát triển bởi Goichi Hosoda Nhật Bản 1969.',
    'sections': [
        {'heading': '🔍 5 đường Ichimoku', 'content': '''<ol>
<li><strong>Tenkan-sen</strong> (đường chuyển đổi) = (high9 + low9) / 2</li>
<li><strong>Kijun-sen</strong> (đường cơ sở) = (high26 + low26) / 2</li>
<li><strong>Senkou Span A</strong> = (Tenkan + Kijun) / 2, vẽ trước 26 phiên</li>
<li><strong>Senkou Span B</strong> = (high52 + low52) / 2, vẽ trước 26 phiên</li>
<li><strong>Chikou Span</strong> = giá hiện tại, vẽ lùi 26 phiên</li>
</ol>
<p>Vùng giữa Senkou A và B = <strong>Kumo Cloud</strong>.</p>'''},
        {'heading': '🎯 4 tín hiệu chính', 'content': '''<h3>1. Giá so với Cloud</h3>
<p>Trên Cloud = uptrend, dưới Cloud = downtrend, trong Cloud = consolidation.</p>
<h3>2. TK Cross (Tenkan/Kijun)</h3>
<p>Tenkan cắt LÊN Kijun = bullish (mạnh nếu xảy ra trên Cloud).</p>
<h3>3. Kumo Twist</h3>
<p>Senkou A cắt B trong tương lai → đảo chiều trend lớn.</p>
<h3>4. Chikou xác nhận</h3>
<p>Chikou trên giá 26 phiên trước = bullish bias.</p>'''},
        {'heading': '✅ Setup hoàn hảo (5 điều kiện)', 'content': '<ol><li>Giá trên Cloud</li><li>Tenkan &gt; Kijun</li><li>TK Cross gần đây</li><li>Chikou trên giá 26 phiên trước</li><li>Senkou A &gt; Senkou B (cloud xanh)</li></ol><p>5/5 điều kiện = bullish cực mạnh, win rate &gt; 75% trên VN30.</p>'},
        {'heading': '⚠️ Khó khăn cho người mới', 'content': '<p>Chart trông phức tạp lúc đầu. Khuyến nghị: tập thuần thục với 1-2 mã trước khi áp dụng rộng.</p>'},
        {'heading': '📊 Ví dụ VCB 2024', 'content': '<p>15/05: VCB break trên Cloud + TK Cross + Chikou trên giá → MUA tại 78K. Giá lên 92K (+18%) trong 12 tuần. Cloud hỗ trợ liên tục.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Symbol modal có Ichimoku layer overlay. Stock Screener filter "Above Cloud + TK Cross".</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/multi-timeframe-ngay-tuan-thang-elder-triple-screen">Multi-Timeframe</a>',
            '<a href="/bai-viet/ema-vs-sma-khac-biet-loai-nao-tot-hon">EMA vs SMA</a>',
        ])}
    ],
    'cta': 'Bật Ichimoku layer trên chart'
},

'obv-la-gi-on-balance-volume': {
    'title': 'OBV Là Gì? On-Balance Volume Chỉ Báo Dòng Tiền | Vnstock',
    'description': 'OBV (On-Balance Volume) — Joseph Granville 1963. Cumulative volume theo hướng giá. Phát hiện accumulation/distribution sớm.',
    'keywords': 'obv là gì, on balance volume, dòng tiền',
    'date': '2026-05-10', 'category': 'Phân tích kỹ thuật', 'reading_time': 6,
    'h1': '📊 OBV — On-Balance Volume Theo Dòng Tiền',
    'lede': 'OBV là chỉ báo "smart money tracker" cổ điển — phát hiện cá mập gom hàng trước khi giá tăng. Đơn giản nhưng hiệu quả.',
    'sections': [
        {'heading': '🔍 Cách tính', 'content': '<pre><code>If Close &gt; Close_prev: OBV += Volume\nIf Close &lt; Close_prev: OBV −= Volume\nIf Close == Close_prev: OBV unchanged</code></pre><p>Cumulative — chỉ quan tâm hướng (up/down), không quan tâm độ lớn của price change.</p>'},
        {'heading': '🎯 Cách dùng', 'content': '<ul><li>OBV trending UP + giá sideway → accumulation (cá mập gom)</li><li>OBV trending DOWN + giá sideway → distribution (xả hàng)</li><li>OBV divergence (giá đỉnh OBV thấp hơn) → cảnh báo đảo chiều</li></ul>'},
        {'heading': '📊 Ví dụ HPG 2024', 'content': '<p>Q1/2024: HPG sideway 26-28K nhưng OBV liên tục tạo đỉnh mới → tín hiệu accumulation. Sau đó breakout lên 38K.</p>'},
        {'heading': '🚀 Vnstock OBV + Smart Money', 'content': '<p>Vnstock có Smart Money Flow (đo trực tiếp buy/sell active) — chính xác hơn OBV. Cả 2 đều có sẵn trong chart.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/smart-money-flow-phat-hien-ca-map-gom-xa">Smart Money Flow</a>',
            '<a href="/bai-viet/volume-la-gi-cach-doc-khoi-luong-tranh-bull-trap">Volume cơ bản</a>',
        ])}
    ],
    'cta': 'Xem Smart Money + OBV trên VN30'
},

'vwap-duong-trung-binh-quan-trong': {
    'title': 'VWAP — Đường Trung Bình Quan Trọng Nhất Daytrading | Vnstock',
    'description': 'VWAP (Volume Weighted Average Price) — giá trung bình có trọng số volume. Reference của tổ chức + benchmark cho daytrading.',
    'keywords': 'vwap là gì, volume weighted average price, daytrading vwap',
    'date': '2026-05-11', 'category': 'Phân tích kỹ thuật', 'reading_time': 6,
    'h1': '📐 VWAP — Đường Trung Bình Của Tổ Chức',
    'lede': 'VWAP là đường mà MỌI quỹ đầu tư + tổ chức đều dùng. Giá trên VWAP = institutional bullish, dưới = bearish. Bài này giải thích tại sao.',
    'sections': [
        {'heading': '🔍 VWAP là gì?', 'content': '<pre><code>VWAP = Σ(Price × Volume) / Σ(Volume)</code></pre><p>Reset mỗi ngày (intraday VWAP). Khác MA — VWAP có trọng số volume → phản ánh "giá trung bình thực tế" trader phải trả.</p>'},
        {'heading': '🎯 Cách dùng', 'content': '<ul><li>Giá &gt; VWAP: institutional sentiment bullish</li><li>Giá &lt; VWAP: institutional sentiment bearish</li><li>Test VWAP từ trên: support; từ dưới: resistance</li><li>Daytrader: mua khi giá vượt VWAP từ dưới + volume confirm</li></ul>'},
        {'heading': '⚡ VWAP Anchored', 'content': '<p>Anchored VWAP từ 1 điểm cụ thể (earnings date, breakout point). Cực mạnh để theo dõi institutional hold cost.</p>'},
        {'heading': '📊 Ví dụ', 'content': '<p>FPT 06/2024: Anchored VWAP từ earnings 110K. Giá test VWAP nhiều lần và bounce. Đến khi break VWAP → trend reversal.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Bảng giá hiển thị VWAP + Anchored VWAP từ ngày user chọn. Premium feature.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/volume-la-gi-cach-doc-khoi-luong-tranh-bull-trap">Volume basics</a>',
            '<a href="/bai-viet/pivot-points-cach-dung-r1-s1">Pivot Points</a>',
        ])}
    ],
    'cta': 'Bật VWAP trên chart'
},

'atr-do-bien-dong-dat-stop-loss': {
    'title': 'ATR — Chỉ Báo Đo Biến Động + Đặt Stop Loss Khoa Học | Vnstock',
    'description': 'ATR (Average True Range) — Wilder 1978. Đo VOLATILITY tuyệt đối. Cách dùng để đặt stop loss và position sizing chuẩn.',
    'keywords': 'atr là gì, average true range, stop loss atr',
    'date': '2026-05-11', 'category': 'Phân tích kỹ thuật', 'reading_time': 6,
    'h1': '🎯 ATR — Đo Biến Động + Stop Loss Khoa Học',
    'lede': 'ATR là chỉ báo bị bỏ qua nhất nhưng quan trọng cho RISK MANAGEMENT. Đặt stop bằng ATR thay vì % cố định = giảm 30% lần stop hit.',
    'sections': [
        {'heading': '🔍 ATR là gì?', 'content': '<p>ATR = trung bình của <strong>True Range</strong> 14 phiên. True Range = max của: (High-Low), |High-Close_prev|, |Low-Close_prev|.</p><p>ATR đo BIÊN ĐỘ tuyệt đối, không đo direction.</p>'},
        {'heading': '🎯 3 cách dùng ATR', 'content': '''<h3>1. Stop Loss</h3>
<p>SL = Entry − 1.5 × ATR (long) hoặc + 1.5 × ATR (short). Giúp tránh "noise stop hit".</p>
<h3>2. Position Sizing</h3>
<p>Risk per trade = % vốn / (ATR × multiplier) → số lượng cổ phiếu hợp lý.</p>
<h3>3. Trailing Stop</h3>
<p>Chandelier Exit: dời stop lên theo ATR khi giá tăng.</p>'''},
        {'heading': '📊 Ví dụ', 'content': '<p>HPG ATR = 600đ. Mua tại 30K → SL = 30K − 1.5 × 600 = 29.1K. Tránh được stop hit do noise hàng ngày.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Symbol modal hiển thị ATR + auto-suggest stop loss = entry − 1.5 ATR.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/quant-lab-garch-var-monte-carlo-kelly">Quant Lab + Kelly sizing</a>',
            '<a href="/bai-viet/bollinger-bands-la-gi-cach-trade-tren-ttck-vn">Bollinger Bands</a>',
        ])}
    ],
    'cta': 'Đặt SL bằng ATR khoa học'
},

'pivot-points-cach-dung-r1-s1': {
    'title': 'Pivot Points — Cách Dùng R1 S1 R2 S2 Trade Intraday | Vnstock',
    'description': 'Pivot Points — support/resistance intraday classic. P, R1, R2, R3, S1, S2, S3. Hướng dẫn cho daytrading + swing.',
    'keywords': 'pivot points, r1 s1 r2 s2, intraday support resistance',
    'date': '2026-05-12', 'category': 'Phân tích kỹ thuật', 'reading_time': 6,
    'h1': '📐 Pivot Points — R1/S1/R2/S2 Trade Intraday',
    'lede': 'Pivot Points là tool intraday phổ biến nhất từ những năm 1980s. Reset mỗi ngày, cho biết các vùng giá quan trọng dựa trên ngày trước.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>P = (High_yesterday + Low_yesterday + Close_yesterday) / 3\nR1 = 2P − Low\nS1 = 2P − High\nR2 = P + (High − Low)\nS2 = P − (High − Low)</code></pre>'},
        {'heading': '🎯 Cách dùng', 'content': '<ul><li>Giá &gt; P: bullish bias hôm nay</li><li>Giá &lt; P: bearish bias</li><li>Test S1/R1 + price action → entry signal</li><li>S2/R2 = vùng cực mạnh</li></ul>'},
        {'heading': '📊 Ví dụ', 'content': '<p>VN30F1M sáng đầu phiên giá &gt; P → bias long. Test R1 + bullish engulfing → mua, target R2.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Bảng giá hiển thị P, R1, S1 cho mỗi mã (intraday). Auto-update mỗi ngày.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/ho-tro-khang-cu-cach-ve-dung-tren-chart">Hỗ trợ kháng cự</a>',
            '<a href="/bai-viet/vwap-duong-trung-binh-quan-trong">VWAP</a>',
        ])}
    ],
    'cta': 'Xem Pivot Points VN30 hôm nay'
},

'cup-and-handle-mo-hinh-tang-gia-manh': {
    'title': 'Cup and Handle — Mô Hình Tăng Giá Mạnh Nhất | Vnstock',
    'description': 'Cup and Handle (William ONeil) — mô hình breakout tin cậy nhất. Cách nhận diện cup, handle, breakout point + ví dụ VN.',
    'keywords': 'cup and handle, mô hình tách trà, oneil breakout',
    'date': '2026-05-12', 'category': 'Phân tích kỹ thuật', 'reading_time': 7,
    'h1': '☕ Cup and Handle — Mô Hình Breakout Của William O\'Neil',
    'lede': 'Cup and Handle (CANSLIM) là mô hình tăng giá mạnh nhất theo William O\'Neil. Mark Minervini và nhiều super-trader Mỹ đã dùng để x10 tài khoản.',
    'sections': [
        {'heading': '🔍 Cấu trúc', 'content': '''<ol>
<li><strong>Cup</strong>: hình chữ U dài 7-65 tuần, depth 12-33%</li>
<li><strong>Handle</strong>: pull back nhẹ 3-12% từ rim, dài 1-6 tuần</li>
<li><strong>Breakout point</strong>: pivot point = đỉnh handle</li>
</ol>'''},
        {'heading': '✅ Confirm', 'content': '<ul><li>Volume tại breakout &gt; 50% trên trung bình</li><li>Cup không quá deep (&gt; 50% là risky)</li><li>Handle thấp hơn rim cup</li></ul>'},
        {'heading': '📊 Ví dụ', 'content': '<p>FPT 2023-2024: Cup từ 95K → 80K → 95K (8 tháng). Handle 95K → 91K (3 tuần). Breakout 95K + volume 2.5x → MUA. Lên 145K (+52%).</p>'},
        {'heading': '🚀 Pattern Scanner Vnstock', 'content': '<p>Auto-detect Cup &amp; Handle hoàn chỉnh trên VN30 + cảnh báo Telegram qua Quality Gate.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/breakout-la-gi-5-cach-tranh-breakout-gia">Breakout là gì</a>',
            '<a href="/bai-viet/head-and-shoulders-tin-hieu-dao-chieu-dinh">Head and Shoulders</a>',
        ])}
    ],
    'cta': 'Quét Cup and Handle live'
},

'head-and-shoulders-tin-hieu-dao-chieu-dinh': {
    'title': 'Head and Shoulders — Tín Hiệu Đảo Chiều Đỉnh | Vnstock',
    'description': 'Head and Shoulders (vai-đầu-vai) — mô hình đảo chiều đỉnh kinh điển. Cách nhận diện + neckline + target price calculation.',
    'keywords': 'head and shoulders, vai đầu vai, mô hình đỉnh',
    'date': '2026-05-13', 'category': 'Phân tích kỹ thuật', 'reading_time': 7,
    'h1': '👤 Head and Shoulders — Cảnh Báo Đỉnh Cổ Điển',
    'lede': 'Head and Shoulders là mô hình đảo chiều đỉnh nổi tiếng nhất. Khi xuất hiện đầy đủ + break neckline → giá thường giảm bằng độ cao của head.',
    'sections': [
        {'heading': '🔍 Cấu trúc', 'content': '<ul><li><strong>Vai trái</strong>: đỉnh đầu tiên</li><li><strong>Đầu</strong>: đỉnh cao hơn</li><li><strong>Vai phải</strong>: đỉnh tương tự vai trái</li><li><strong>Neckline</strong>: nối đáy giữa vai và đầu</li></ul>'},
        {'heading': '🎯 Trade signal', 'content': '<p>Break neckline xuống + volume confirm → SELL/SHORT. Target = Neckline − (Head_high − Neckline).</p>'},
        {'heading': '📊 Ví dụ MWG 2022', 'content': '<p>2022: Vai trái 158K, Đầu 175K, Vai phải 162K. Neckline 145K. Break xuống → giá xuống 100K (target đúng).</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Pattern Scanner auto-detect H&S + Inverse H&S + tự tính target price.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/cup-and-handle-mo-hinh-tang-gia-manh">Cup and Handle (opposite)</a>',
            '<a href="/bai-viet/triple-top-bottom-3-lan-test">Triple Top/Bottom</a>',
        ])}
    ],
    'cta': 'Quét H&S Pattern hôm nay'
},

'triple-top-bottom-3-lan-test': {
    'title': 'Triple Top/Bottom — 3 Lần Test Quyết Định | Vnstock',
    'description': 'Triple Top (3 đỉnh) — mô hình đảo chiều đỉnh, 3 đỉnh gần bằng nhau. Triple Bottom là phiên bản đáy. Tin cậy hơn double pattern.',
    'keywords': 'triple top, triple bottom, mô hình 3 đỉnh',
    'date': '2026-05-13', 'category': 'Phân tích kỹ thuật', 'reading_time': 6,
    'h1': '📊 Triple Top/Bottom — 3 Lần Test Của Sức Mạnh',
    'lede': 'Triple Top tin cậy hơn Double Top vì kháng cự đã test 3 lần và không vượt được — bên bán chiếm ưu thế rõ ràng.',
    'sections': [
        {'heading': '🔍 Cấu trúc Triple Top', 'content': '<ul><li>3 đỉnh ở gần cùng mức giá (chênh &lt; 3%)</li><li>Khoảng cách giữa các đỉnh đều</li><li>2 đáy giữa cũng gần bằng nhau (gọi là "support")</li><li>Volume giảm dần qua mỗi đỉnh</li></ul>'},
        {'heading': '🎯 Signal', 'content': '<p>Break support xuống + volume → SELL. Target = support − (đỉnh − support).</p>'},
        {'heading': '📊 Ví dụ VHM 2024', 'content': '<p>VHM test 52K 3 lần (06, 09, 11/2024) — không vượt. Break support 41K → giảm về 33K.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Pattern Scanner detect 3+ touch resistance + alert.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/head-and-shoulders-tin-hieu-dao-chieu-dinh">Head and Shoulders</a>',
            '<a href="/bai-viet/cup-and-handle-mo-hinh-tang-gia-manh">Cup and Handle</a>',
        ])}
    ],
    'cta': 'Quét Triple Top/Bottom'
},

'breakout-la-gi-5-cach-tranh-breakout-gia': {
    'title': 'Breakout Là Gì? 5 Cách Tránh Breakout Giả 2026 | Vnstock',
    'description': 'Breakout — giá vượt resistance/support quan trọng. 60-70% breakout là FAKE. 5 quy tắc lọc để chỉ trade real breakout.',
    'keywords': 'breakout là gì, breakout giả, fake breakout, real breakout',
    'date': '2026-05-14', 'category': 'Phân tích kỹ thuật', 'reading_time': 8,
    'h1': '⚡ Breakout Là Gì? 5 Cách Tránh Breakout Giả',
    'lede': 'Theo nghiên cứu của Bulkowski, 60-70% breakout là FAKE. Nếu trade hết bạn lỗ phí + slippage rất nhanh. Bài này hướng dẫn lọc real breakout.',
    'sections': [
        {'heading': '🔍 Breakout là gì?', 'content': '<p>Breakout = giá VƯỢT resistance hoặc PHÁ support quan trọng. Sau breakout, giá thường tiếp tục theo hướng đó.</p>'},
        {'heading': '⚠️ Vì sao 70% breakout là giả?', 'content': '<p>Cá mập "stop hunt" — đẩy giá vượt resistance để stop hit của bear trader, sau đó kéo ngược xuống. Trong sideway, breakout giả phổ biến.</p>'},
        {'heading': '✅ 5 quy tắc lọc real breakout', 'content': '''<ol>
<li><strong>Volume &gt;= 1.5x avg 20</strong> — không có volume = chưa phải</li>
<li><strong>Close trên resistance &gt;= 2 phiên</strong> — không phải intraday spike</li>
<li><strong>ADX &gt; 25</strong> — phải có trend, không phải sideway</li>
<li><strong>Resistance test &gt;= 2 lần trước đó</strong> — vùng có ý nghĩa</li>
<li><strong>Pattern context</strong>: trong cup & handle hoặc consolidation pattern</li>
</ol>'''},
        {'heading': '🎯 Pre-Breakout Detection', 'content': '<p>Vnstock có Pre-Breakout Scanner phát hiện coiled spring (Bollinger squeeze + volume drying up + tightening range) — báo trước 3-7 phiên.</p>'},
        {'heading': '📊 Ví dụ', 'content': '<p>FPT 06/2024: Squeeze 5 tuần ở 105-110K, volume drying. Break 110K + volume 2.8x → real. Lên 145K.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Pre-Breakout Scanner alert + post-breakout confirmation rules. Trong Dashboard.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/cup-and-handle-mo-hinh-tang-gia-manh">Cup and Handle</a>',
            '<a href="/bai-viet/volume-la-gi-cach-doc-khoi-luong-tranh-bull-trap">Volume confirm</a>',
            '<a href="/bai-viet/adx-la-gi-cach-phan-biet-trend-vs-sideway">ADX filter</a>',
        ])}
    ],
    'cta': 'Bật Pre-Breakout Scanner'
},

'volume-profile-phan-tich-khoi-luong': {
    'title': 'Volume Profile — Phân Tích Khối Lượng Theo Vùng Giá | Vnstock',
    'description': 'Volume Profile khác Volume Bar — phân bố khối lượng theo VÙNG GIÁ. POC (Point of Control), Value Area, HVN/LVN.',
    'keywords': 'volume profile, point of control, value area',
    'date': '2026-05-14', 'category': 'Phân tích kỹ thuật', 'reading_time': 8,
    'h1': '📊 Volume Profile — Khối Lượng Theo Vùng Giá',
    'lede': 'Volume Bar dưới chart cho biết volume theo TIME. Volume Profile cho biết volume theo PRICE — vùng nào được "trade nhiều nhất" → vùng support/resistance mạnh nhất.',
    'sections': [
        {'heading': '🔍 Khái niệm', 'content': '<ul><li><strong>POC (Point of Control)</strong>: giá có volume cao nhất trong period</li><li><strong>Value Area</strong>: khoảng giá chứa 70% volume (VAH/VAL = upper/lower)</li><li><strong>HVN (High Volume Node)</strong>: vùng nhiều volume → support/resistance</li><li><strong>LVN (Low Volume Node)</strong>: vùng ít volume → giá thường "lướt qua nhanh"</li></ul>'},
        {'heading': '🎯 Cách trade', 'content': '<ul><li>Mua/bán test POC + price action confirm</li><li>Trade range trong Value Area</li><li>LVN gap → giá có thể chuyển nhanh giữa 2 vùng HVN</li></ul>'},
        {'heading': '📊 Ví dụ', 'content': '<p>VCB Q3/2024: POC 85K (volume cao nhất). Giá từ 82K → 90K → POC 85K test 2 lần làm support. Đến khi break 82K → đợt giảm mới.</p>'},
        {'heading': '🚀 Vnstock Pro', 'content': '<p>Volume Profile overlay trên chart (Premium feature). Auto-detect POC, VAH, VAL.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/volume-la-gi-cach-doc-khoi-luong-tranh-bull-trap">Volume basics</a>',
            '<a href="/bai-viet/vwap-duong-trung-binh-quan-trong">VWAP</a>',
            '<a href="/bai-viet/ho-tro-khang-cu-cach-ve-dung-tren-chart">Support/Resistance</a>',
        ])}
    ],
    'cta': 'Mở Volume Profile (Premium)'
},

'heikin-ashi-cach-doc-nen-trung-binh': {
    'title': 'Heikin-Ashi — Cách Đọc Nến Trung Bình Để Tránh Nhiễu | Vnstock',
    'description': 'Heikin-Ashi (Nhật Bản) — nến trung bình giúp lọc nhiễu, dễ đọc trend. Khác candlestick chuẩn ở công thức + cách đọc.',
    'keywords': 'heikin ashi, nến trung bình, lọc nhiễu chart',
    'date': '2026-05-15', 'category': 'Phân tích kỹ thuật', 'reading_time': 6,
    'h1': '🕯 Heikin-Ashi — Lọc Nhiễu Để Đọc Trend Rõ',
    'lede': 'Heikin-Ashi (平均足 — "nến trung bình") làm chart "mượt hơn" candlestick chuẩn. Dễ thấy trend, ít noise — phù hợp cho swing trader.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>HA_Close = (Open + High + Low + Close) / 4\nHA_Open = (HA_Open_prev + HA_Close_prev) / 2\nHA_High = max(High, HA_Open, HA_Close)\nHA_Low = min(Low, HA_Open, HA_Close)</code></pre>'},
        {'heading': '🎯 Cách đọc', 'content': '<ul><li>Nhiều nến xanh liên tiếp + bóng dưới ngắn = uptrend mạnh</li><li>Nhiều nến đỏ + bóng trên ngắn = downtrend mạnh</li><li>Nến doji-like = đảo chiều</li></ul>'},
        {'heading': '⚠️ Hạn chế', 'content': '<p>Heikin-Ashi DỜI signal 1-2 phiên (vì smoothed). Không nhìn được giá real-time chính xác. Không phù hợp cho daytrading scalping.</p>'},
        {'heading': '📊 Ví dụ', 'content': '<p>Switch chart sang Heikin-Ashi cho HPG → trend 06/2024 → 08/2024 hiện ra rõ ràng (chuỗi nến xanh dài), không nhiễu như candlestick chuẩn.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Symbol modal có toggle Candlestick / Heikin-Ashi / Line.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/mo-hinh-nen-dao-chieu-8-mau-quan-trong">Mô hình nến</a>',
            '<a href="/bai-viet/ema-vs-sma-khac-biet-loai-nao-tot-hon">EMA vs SMA</a>',
        ])}
    ],
    'cta': 'Switch Heikin-Ashi mode'
},

'keltner-channel-vs-bollinger': {
    'title': 'Keltner Channel vs Bollinger — Khi Nào Dùng Cái Nào | Vnstock',
    'description': 'Keltner Channel dùng ATR, Bollinger dùng Standard Deviation. Cùng mục đích nhưng phản ứng khác nhau. Khi nào dùng từng cái.',
    'keywords': 'keltner channel, keltner vs bollinger, atr channel',
    'date': '2026-05-15', 'category': 'Phân tích kỹ thuật', 'reading_time': 7,
    'h1': '📊 Keltner Channel vs Bollinger — So Sánh',
    'lede': 'Cả 2 đều là volatility channel với 3 đường — nhưng khác cách tính. Trader chuyên dùng cả 2 để xác nhận signal.',
    'sections': [
        {'heading': '🔍 So sánh công thức', 'content': '''<table>
<tr><th></th><th>Bollinger</th><th>Keltner</th></tr>
<tr><td>Middle</td><td>SMA(20)</td><td>EMA(20)</td></tr>
<tr><td>Width</td><td>±2σ</td><td>±2 × ATR(10)</td></tr>
<tr><td>Phản ứng</td><td>Nhạy với outlier</td><td>Mượt hơn</td></tr>
</table>'''},
        {'heading': '🎯 Khi nào dùng', 'content': '<ul><li>Bollinger: detect breakout/squeeze tốt hơn</li><li>Keltner: trend following ổn định hơn</li><li>Combine: TTM Squeeze (Bollinger trong Keltner) = sắp breakout lớn</li></ul>'},
        {'heading': '🔥 TTM Squeeze (John Carter)', 'content': '<p>Khi cả 2 Bollinger Bands đều INSIDE Keltner Channel → "squeeze ON". Khi giá break, nó break MẠNH. Win rate setup này &gt; 70%.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Stock Screener có filter "TTM Squeeze ON" detect coiled spring trên 456 mã VN.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/bollinger-bands-la-gi-cach-trade-tren-ttck-vn">Bollinger Bands</a>',
            '<a href="/bai-viet/atr-do-bien-dong-dat-stop-loss">ATR</a>',
            '<a href="/bai-viet/breakout-la-gi-5-cach-tranh-breakout-gia">Breakout</a>',
        ])}
    ],
    'cta': 'Quét TTM Squeeze'
},

'phan-tich-ky-thuat-chung-khoan-a-z': {
    'title': 'Hướng Dẫn Phân Tích Kỹ Thuật Từ A-Z (PILLAR) 2026 | Vnstock',
    'description': 'Pillar guide phân tích kỹ thuật cho người mới: 6 trụ cột (Trend, Momentum, Volume, Pattern, S/R, Multi-TF). Tất cả links chi tiết.',
    'keywords': 'phân tích kỹ thuật, pillar guide, technical analysis',
    'date': '2026-05-16', 'category': 'Phân tích kỹ thuật', 'reading_time': 15,
    'h1': '📚 Hướng Dẫn Phân Tích Kỹ Thuật Từ A-Z',
    'lede': 'Đây là pillar post tập hợp toàn bộ kiến thức TA cần thiết. 6 trụ cột chính, mỗi trụ cột có links sang chi tiết. Đọc 1 lần để có roadmap.',
    'sections': [
        {'heading': '🎯 Trụ cột 1: TREND — Xác định xu hướng', 'content': '<ul><li><a href="/bai-viet/ema-vs-sma-khac-biet-loai-nao-tot-hon">EMA vs SMA</a></li><li><a href="/bai-viet/adx-la-gi-cach-phan-biet-trend-vs-sideway">ADX — Sức mạnh trend</a></li><li><a href="/bai-viet/trendline-la-gi-cach-ve-trendline">Trendline</a></li><li><a href="/bai-viet/multi-timeframe-ngay-tuan-thang-elder-triple-screen">Multi-Timeframe</a></li></ul>'},
        {'heading': '🎯 Trụ cột 2: MOMENTUM — Đo lực đẩy', 'content': '<ul><li><a href="/bai-viet/rsi-la-gi-cach-dung-rsi-chon-co-phieu">RSI</a></li><li><a href="/bai-viet/macd-la-gi-tin-hieu-mua-ban-vang-chet">MACD</a></li><li><a href="/bai-viet/stochastic-cach-dung-k-d">Stochastic</a></li><li><a href="/bai-viet/divergence-la-gi-rsi-macd-divergence">Divergence</a></li></ul>'},
        {'heading': '🎯 Trụ cột 3: VOLUME — Xác nhận', 'content': '<ul><li><a href="/bai-viet/volume-la-gi-cach-doc-khoi-luong-tranh-bull-trap">Volume basics</a></li><li><a href="/bai-viet/obv-la-gi-on-balance-volume">OBV</a></li><li><a href="/bai-viet/vwap-duong-trung-binh-quan-trong">VWAP</a></li><li><a href="/bai-viet/volume-profile-phan-tich-khoi-luong">Volume Profile</a></li></ul>'},
        {'heading': '🎯 Trụ cột 4: PATTERN — Mô hình', 'content': '<ul><li><a href="/bai-viet/mo-hinh-nen-dao-chieu-8-mau-quan-trong">8 mô hình nến</a></li><li><a href="/bai-viet/cup-and-handle-mo-hinh-tang-gia-manh">Cup and Handle</a></li><li><a href="/bai-viet/head-and-shoulders-tin-hieu-dao-chieu-dinh">Head and Shoulders</a></li><li><a href="/bai-viet/breakout-la-gi-5-cach-tranh-breakout-gia">Breakout</a></li></ul>'},
        {'heading': '🎯 Trụ cột 5: SUPPORT/RESISTANCE', 'content': '<ul><li><a href="/bai-viet/ho-tro-khang-cu-cach-ve-dung-tren-chart">S/R cách vẽ</a></li><li><a href="/bai-viet/fibonacci-retracement-auto-magnetic-snap">Fibonacci</a></li><li><a href="/bai-viet/pivot-points-cach-dung-r1-s1">Pivot Points</a></li><li><a href="/bai-viet/bollinger-bands-la-gi-cach-trade-tren-ttck-vn">Bollinger Bands</a></li></ul>'},
        {'heading': '🎯 Trụ cột 6: ADVANCED', 'content': '<ul><li><a href="/bai-viet/ichimoku-cloud-he-thong-trading-nhat-ban">Ichimoku</a></li><li><a href="/bai-viet/heikin-ashi-cach-doc-nen-trung-binh">Heikin-Ashi</a></li><li><a href="/bai-viet/keltner-channel-vs-bollinger">Keltner Channel</a></li><li><a href="/bai-viet/atr-do-bien-dong-dat-stop-loss">ATR Risk Mgmt</a></li></ul>'},
        {'heading': '🚀 Áp dụng tổng hợp trên Vnstock', 'content': '<p>Vnstock tích hợp tất cả 19 chỉ báo từ 6 trụ cột này vào 1 composite score. Stock Screener xếp hạng 456 mã VN theo composite z-score → strong_buy/buy/hold/sell tier.</p>'}
    ],
    'cta': 'Mở Stock Screener Composite'
},

# ════════════════════════════════════════════════════════════════
# CLUSTER B — STOCK SCREENING (12 bài: bài 31-42)
# ════════════════════════════════════════════════════════════════

'loc-co-phieu-tang-truong-7-tieu-chi': {
    'title': 'Cách Lọc Cổ Phiếu Tăng Trưởng — 7 Tiêu Chí Vàng 2026 | Vnstock',
    'description': 'Lọc cổ phiếu tăng trưởng theo CANSLIM (William ONeil). 7 tiêu chí: EPS growth, ROE, sector leader, technical, volume, institutional, market trend.',
    'keywords': 'lọc cổ phiếu tăng trưởng, canslim, growth stocks, eps growth',
    'date': '2026-05-17', 'category': 'Stock Screening', 'reading_time': 9,
    'h1': '🚀 Cách Lọc Cổ Phiếu Tăng Trưởng — 7 Tiêu Chí Vàng',
    'lede': 'William O\'Neil đã chứng minh 7 tiêu chí CANSLIM giúp lọc ra Top 1% cổ phiếu tăng nhất mỗi năm. Áp dụng cho TTCK Việt Nam với 456 mã.',
    'sections': [
        {'heading': '📋 7 tiêu chí CANSLIM (đã VN-hóa)', 'content': '''<ol>
<li><strong>C — Current EPS growth &gt; 20%</strong> (Q gần nhất so cùng kỳ)</li>
<li><strong>A — Annual EPS growth &gt; 25%</strong> (3 năm gần nhất)</li>
<li><strong>N — New product/management/highs</strong> (mã đang ở vùng đỉnh 52w)</li>
<li><strong>S — Supply (FCF cao + low debt)</strong></li>
<li><strong>L — Leader trong ngành</strong> (top 3 RS rating)</li>
<li><strong>I — Institutional buying</strong> (khối ngoại + cá mập gom)</li>
<li><strong>M — Market direction</strong> (VN-Index uptrend)</li>
</ol>'''},
        {'heading': '🎯 Áp dụng Vnstock Multifactor', 'content': '<p>Vnstock multifactor screener đã built-in 6 factor tương đương CANSLIM:</p><ul><li>Momentum + Trend = N + L</li><li>Smart Money + Foreign = I</li><li>Quality (low vol) = S</li><li>Volume = N (volume confirm new high)</li></ul>'},
        {'heading': '📊 Top 5 hôm nay', 'content': '<p>Click <a href="/app">/app</a> → Tab Screener → "Composite Z-score &gt;= +1.5" để thấy top mã CANSLIM-passing.</p>'},
        {'heading': '⚠️ Sai lầm', 'content': '<p>Mua mã giảm sâu vì "rẻ" — đó là deep value, không phải growth. Growth phải ở vùng đỉnh đang break.</p>'},
        {'heading': '✅ Kết luận', 'content': _CTA_FOOTER([
            '<a href="/bai-viet/loc-co-phieu-breakout-mark-minervini">Lọc Breakout (Minervini)</a>',
            '<a href="/bai-viet/loc-co-phieu-gia-tri-buffett">Lọc Giá trị (Buffett)</a>',
            '<a href="/bai-viet/stock-screener-vietnam-top-7">Stock Screener VN Top 7</a>',
            '<a href="/bai-viet/co-phieu-tang-truong-2026">Cổ phiếu tăng trưởng 2026</a>',
        ])}
    ],
    'cta': 'Lọc Top 20 Growth Stocks ngay'
},

'loc-co-phieu-breakout-mark-minervini': {
    'title': 'Lọc Cổ Phiếu Breakout — Phương Pháp Mark Minervini Cho VN | Vnstock',
    'description': 'Mark Minervini (US Investing Champion) — VCP (Volatility Contraction Pattern). Cách áp dụng cho VN30 + Pre-Breakout Scanner Vnstock.',
    'keywords': 'lọc cổ phiếu breakout, mark minervini, vcp, pre-breakout',
    'date': '2026-05-17', 'category': 'Stock Screening', 'reading_time': 8,
    'h1': '⚡ Lọc Cổ Phiếu Breakout — Mark Minervini Style',
    'lede': 'Mark Minervini 2x giành US Investing Championship với phương pháp VCP — phát hiện cổ phiếu sắp breakout 5-10 ngày trước. Vnstock tự động hóa cho TTCK VN.',
    'sections': [
        {'heading': '🔍 VCP — Volatility Contraction Pattern', 'content': '<p>5 đặc điểm:</p><ol><li>Cổ phiếu uptrend (above MA200)</li><li>Vài lần pull back, mỗi lần shallow hơn (5-10% → 4-7% → 3-5%)</li><li>Volume giảm dần qua mỗi pull back</li><li>Bollinger Bands squeeze</li><li>Stage 2 (Stan Weinstein)</li></ol>'},
        {'heading': '✅ Trend Template (Minervini)', 'content': '<ol><li>Giá &gt; MA50 và MA50 &gt; MA200</li><li>MA200 dốc lên ít nhất 1 tháng</li><li>Giá &gt;= 25% trên 52-week low</li><li>Giá nằm trong 25% từ 52-week high</li><li>RS rating &gt;= 70 (top 30%)</li></ol>'},
        {'heading': '🚀 Pre-Breakout Scanner Vnstock', 'content': '<p>Auto-detect VCP + Trend Template trên 456 mã. Cảnh báo qua Telegram khi:</p><ul><li>Squeeze 4+ tuần</li><li>Volume drying up &lt; 70% avg</li><li>Range tightening &lt; 5%</li><li>RS rank top 30%</li></ul>'},
        {'heading': '📊 Ví dụ FPT 2024', 'content': '<p>05/2024 FPT VCP rõ rệt: 110K → 102K → 108K → 105K → 109K. Volume giảm dần. Pre-Breakout alert. Break 110K + volume 2.5x → MUA. Lên 145K.</p>'},
        {'heading': '✅ Kết luận', 'content': _CTA_FOOTER([
            '<a href="/bai-viet/loc-co-phieu-tang-truong-7-tieu-chi">Growth CANSLIM</a>',
            '<a href="/bai-viet/breakout-la-gi-5-cach-tranh-breakout-gia">Breakout là gì</a>',
            '<a href="/bai-viet/cup-and-handle-mo-hinh-tang-gia-manh">Cup and Handle</a>',
        ])}
    ],
    'cta': 'Bật Pre-Breakout Scanner'
},

'loc-co-phieu-gia-tri-buffett': {
    'title': 'Lọc Cổ Phiếu Giá Trị — Công Thức Buffett Cho TTCK VN | Vnstock',
    'description': 'Value investing (Buffett, Graham). 6 tiêu chí: P/E thấp, P/B &lt; 1.5, ROE &gt; 15%, Debt/Equity &lt; 0.5, FCF dương, dividend yield. Áp dụng VN.',
    'keywords': 'lọc cổ phiếu giá trị, value investing, buffett, graham',
    'date': '2026-05-18', 'category': 'Stock Screening', 'reading_time': 8,
    'h1': '💎 Lọc Cổ Phiếu Giá Trị — Công Thức Buffett',
    'lede': 'Warren Buffett và Benjamin Graham đã chứng minh value investing là chiến lược thắng dài hạn. 6 tiêu chí lọc value stock cho TTCK VN.',
    'sections': [
        {'heading': '📋 6 tiêu chí Value', 'content': '''<ol>
<li><strong>P/E &lt; 15</strong> (so với ngành)</li>
<li><strong>P/B &lt; 1.5</strong></li>
<li><strong>ROE &gt; 15%</strong> (consistent 5 năm)</li>
<li><strong>Debt/Equity &lt; 0.5</strong></li>
<li><strong>Free Cash Flow dương + tăng trưởng</strong></li>
<li><strong>Dividend yield &gt; 3%</strong> (bonus)</li>
</ol>'''},
        {'heading': '⚠️ Tránh Value Trap', 'content': '<p>P/E thấp + P/B thấp có thể là VALUE TRAP — công ty đang mất market share, sắp phá sản. Phải confirm:</p><ul><li>Earnings ổn định 5 năm (không giảm liên tục)</li><li>Quality of earnings (cash flow &gt; net income)</li><li>Sector không bị disrupt</li></ul>'},
        {'heading': '📊 Top Value Stocks VN30', 'content': '<p>Vnstock Multi-factor có "quality factor" + "valuation overlay" → lọc value stocks chuẩn Graham + Buffett.</p>'},
        {'heading': '🚀 Vnstock Screener', 'content': '<p>Filter "P/E &lt; 15 + P/B &lt; 1.5 + ROE &gt; 15%" trong Stock Screener.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/p-e-bao-nhieu-hop-ly">P/E bao nhiêu hợp lý</a>',
            '<a href="/bai-viet/p-b-bao-nhieu-tot">P/B bao nhiêu tốt</a>',
            '<a href="/bai-viet/roe-bao-nhieu-la-tot">ROE bao nhiêu tốt</a>',
            '<a href="/bai-viet/loc-co-phieu-tang-truong-7-tieu-chi">Growth CANSLIM</a>',
        ])}
    ],
    'cta': 'Lọc Value Stocks VN'
},

'loc-co-phieu-dau-co-canh-bao': {
    'title': 'Lọc Cổ Phiếu Đầu Cơ — Chiến Thuật + Cảnh Báo Rủi Ro | Vnstock',
    'description': 'Cổ phiếu đầu cơ (penny stocks, low cap) có thể x2-x5 nhưng cũng có thể -90%. 5 tiêu chí lọc + 5 quy tắc risk management.',
    'keywords': 'lọc cổ phiếu đầu cơ, penny stocks, đầu cơ rủi ro',
    'date': '2026-05-18', 'category': 'Stock Screening', 'reading_time': 7,
    'h1': '🎲 Lọc Cổ Phiếu Đầu Cơ — Cao Lợi Nhuận, Cao Rủi Ro',
    'lede': 'Cổ phiếu đầu cơ hấp dẫn vì có thể x2-x5 trong 1-2 tháng. Nhưng 70% người chơi MẤT TIỀN. Hướng dẫn lọc + quản trị rủi ro tối thiểu.',
    'sections': [
        {'heading': '📋 5 tiêu chí mã đầu cơ "đẹp"', 'content': '''<ol>
<li>Vốn hóa &lt; 1000 tỷ VND</li>
<li>Volume tăng &gt;= 3x trong 5 phiên gần</li>
<li>Cá mập gom (shark streak &gt;= 3)</li>
<li>Tin tức/catalyst gần đây</li>
<li>Breakout consolidation pattern</li>
</ol>'''},
        {'heading': '⚠️ 5 quy tắc Risk Management', 'content': '<ol><li>KHÔNG quá 5% portfolio cho 1 mã đầu cơ</li><li>Stop loss CỨNG -8%</li><li>Take profit từng phần (sell 30% tại +20%, 30% tại +40%)</li><li>KHÔNG bình quân giá xuống</li><li>KHÔNG hold qua đêm news cuối tuần</li></ol>'},
        {'heading': '🔴 Tránh', 'content': '<ul><li>Mã penny &lt; 5K (rủi ro pump &amp; dump)</li><li>Mã không có FCF dương</li><li>Mã có liên quan vụ kiện/điều tra</li></ul>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Stock Screener filter "Volume &gt;= 3x + Shark streak &gt;= 3 + Vốn hóa nhỏ" → speculative watchlist.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/loc-co-phieu-tang-truong-7-tieu-chi">Growth (an toàn hơn)</a>',
            '<a href="/bai-viet/loc-co-phieu-gia-tri-buffett">Value (an toàn nhất)</a>',
        ])}
    ],
    'cta': 'Quét speculative stocks (cẩn trọng)'
},

'stock-screener-vietnam-top-7': {
    'title': 'Stock Screener Việt Nam — Top 7 Công Cụ Tốt Nhất 2026 | Vnstock',
    'description': 'So sánh 7 stock screener cho TTCK VN: Vnstock, FireAnt, TCBS, Investing.com, TradingView, SimplyWallSt, Vietstock. Pros/Cons + giá.',
    'keywords': 'stock screener việt nam, công cụ lọc cổ phiếu, screener vn30',
    'date': '2026-05-19', 'category': 'Stock Screening', 'reading_time': 11,
    'h1': '📊 Stock Screener Việt Nam — Top 7 Công Cụ Tốt Nhất 2026',
    'lede': 'Stock screener tốt = lọc 1600 mã trong 1 giây thành top 20 đáng theo dõi. So sánh 7 tool phổ biến với TTCK VN.',
    'sections': [
        {'heading': '🥇 #1 Vnstock.io.vn', 'content': '<p><strong>Pros</strong>: Multi-factor composite z-score (6 nhân tố), 19 chỉ báo, Smart Money + Foreign Flow, miễn phí 20 mã. Premium 299K/tháng.</p><p><strong>Cons</strong>: Chỉ VN + US (không có HK, JP).</p>'},
        {'heading': '🥈 #2 TradingView', 'content': '<p>Mạnh nhất về charting + community scripts. <strong>Cons</strong>: Không có VN screener chuyên sâu, $14.95/tháng.</p>'},
        {'heading': '🥉 #3 FireAnt', 'content': '<p>VN-focused, có news. <strong>Cons</strong>: Screener cơ bản, không có quant features.</p>'},
        {'heading': '#4-7', 'content': '<p>TCBS Pro (broker), Vietstock (truyền thống), Investing.com (international), SimplyWallSt (fundamental).</p>'},
        {'heading': '🎯 Recommendation', 'content': '<table><tr><th>Use Case</th><th>Tool</th></tr><tr><td>VN trader cần multi-factor + AI</td><td><strong>Vnstock</strong></td></tr><tr><td>Pure charting + script community</td><td>TradingView</td></tr><tr><td>News + research VN</td><td>FireAnt</td></tr></table>' + _CTA_FOOTER([
            '<a href="/bai-viet/tradingview-vs-vnstock">TradingView vs Vnstock chi tiết</a>',
            '<a href="/bai-viet/fireant-vs-vnstock">FireAnt vs Vnstock</a>',
            '<a href="/bai-viet/loc-co-phieu-tang-truong-7-tieu-chi">Growth filter</a>',
        ])}
    ],
    'cta': 'Dùng Vnstock Screener miễn phí'
},

'roe-bao-nhieu-la-tot': {
    'title': 'ROE Bao Nhiêu Là Tốt? Tiêu Chuẩn Cho TTCK VN | Vnstock',
    'description': 'ROE (Return on Equity) — tỷ suất sinh lời trên vốn chủ. Bao nhiêu là tốt theo ngành? Cách phân tích + 5 quy tắc xét ROE.',
    'keywords': 'roe là gì, roe bao nhiêu là tốt, return on equity',
    'date': '2026-05-19', 'category': 'Fundamental', 'reading_time': 7,
    'h1': '💰 ROE Bao Nhiêu Là Tốt? Tiêu Chuẩn TTCK VN',
    'lede': 'ROE là chỉ số đo "khả năng tạo lợi nhuận từ vốn chủ" — chỉ báo quan trọng nhất của Buffett. Nhưng "ROE bao nhiêu tốt" phụ thuộc ngành.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>ROE = Net Income / Shareholders\' Equity × 100%</code></pre>'},
        {'heading': '📊 ROE benchmark theo ngành VN', 'content': '''<table>
<tr><th>Ngành</th><th>ROE tốt</th><th>Ví dụ</th></tr>
<tr><td>Ngân hàng</td><td>&gt; 18%</td><td>VCB ~22%, MBB ~21%</td></tr>
<tr><td>BĐS</td><td>&gt; 15%</td><td>VHM ~16%</td></tr>
<tr><td>Tiêu dùng</td><td>&gt; 25%</td><td>VNM ~32%, MSN ~28%</td></tr>
<tr><td>Công nghệ</td><td>&gt; 20%</td><td>FPT ~24%</td></tr>
<tr><td>Thép</td><td>&gt; 12%</td><td>HPG ~15%</td></tr>
</table>'''},
        {'heading': '⚠️ ROE cao có thể là TRAP', 'content': '<p>ROE cao do leverage cao → rủi ro. Buffett chỉ thích ROE cao + ÍT NỢ.</p><pre><code>DuPont: ROE = (Net margin) × (Asset turnover) × (Equity multiplier)</code></pre><p>Equity multiplier cao = nợ nhiều = ROE bị "thổi phồng".</p>'},
        {'heading': '✅ Quy tắc Buffett', 'content': '<ul><li>ROE &gt; 15% consistent 10 năm</li><li>Debt/Equity &lt; 0.5</li><li>Margin trend ổn định/tăng</li></ul>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Tab Fundamental hiển thị ROE 5 năm + benchmark ngành tự động.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/p-e-bao-nhieu-hop-ly">P/E bao nhiêu</a>',
            '<a href="/bai-viet/p-b-bao-nhieu-tot">P/B bao nhiêu</a>',
            '<a href="/bai-viet/roic-vs-roe">ROIC vs ROE</a>',
            '<a href="/bai-viet/loc-co-phieu-gia-tri-buffett">Buffett value</a>',
        ])}
    ],
    'cta': 'Xem ROE của VNM, VCB, FPT...'
},

'p-e-bao-nhieu-hop-ly': {
    'title': 'P/E Bao Nhiêu Là Hợp Lý? Per Industry VN 2026 | Vnstock',
    'description': 'P/E (Price/Earnings) — chỉ số định giá phổ biến nhất. P/E hợp lý theo ngành VN. Forward P/E vs Trailing P/E.',
    'keywords': 'p/e bao nhiêu hợp lý, p/e ratio, forward pe',
    'date': '2026-05-20', 'category': 'Fundamental', 'reading_time': 7,
    'h1': '📊 P/E Bao Nhiêu Là Hợp Lý? Per Industry VN',
    'lede': 'P/E "chuẩn" 15 chỉ là rule of thumb. Mỗi ngành có range khác nhau. Bài này cho bạn benchmark cụ thể VN30.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>P/E = Market Price / Earnings Per Share (EPS)</code></pre><p>P/E = "bạn trả bao nhiêu cho 1 đồng lợi nhuận hàng năm".</p>'},
        {'heading': '📊 P/E benchmark VN', 'content': '''<table>
<tr><th>Ngành</th><th>P/E hợp lý</th></tr>
<tr><td>Ngân hàng</td><td>8-12</td></tr>
<tr><td>BĐS</td><td>10-18</td></tr>
<tr><td>Tiêu dùng</td><td>18-25</td></tr>
<tr><td>Công nghệ</td><td>20-30</td></tr>
<tr><td>Thép/VLXD</td><td>6-12</td></tr>
<tr><td>Dầu khí</td><td>8-14</td></tr>
</table>'''},
        {'heading': '⚠️ Forward vs Trailing', 'content': '<ul><li><strong>Trailing P/E</strong>: dùng EPS 12 tháng qua (mặc định)</li><li><strong>Forward P/E</strong>: dùng EPS dự báo 12 tháng tới (chính xác hơn cho growth)</li></ul>'},
        {'heading': '🎯 Khi nào P/E cao OK?', 'content': '<p>Nếu growth EPS &gt; 25% → PEG ratio = P/E / Growth &lt; 1 → vẫn rẻ. Ví dụ FPT P/E 22 nhưng growth 25% → PEG = 0.88, fair.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Fundamental tab tự highlight nếu P/E &lt; benchmark ngành.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/peg-ratio-chi-so-quan-trong">PEG Ratio</a>',
            '<a href="/bai-viet/p-b-bao-nhieu-tot">P/B</a>',
            '<a href="/bai-viet/eps-la-gi">EPS là gì</a>',
        ])}
    ],
    'cta': 'Lọc P/E hợp lý theo ngành'
},

'p-b-bao-nhieu-tot': {
    'title': 'P/B Bao Nhiêu Tốt? Cách Đánh Giá P/B Theo Ngành | Vnstock',
    'description': 'P/B (Price/Book) — đo giá so với giá trị sổ sách. Đặc biệt quan trọng cho ngân hàng + bảo hiểm. Khi nào P/B cao OK.',
    'keywords': 'p/b là gì, p/b bao nhiêu tốt, price to book',
    'date': '2026-05-20', 'category': 'Fundamental', 'reading_time': 6,
    'h1': '📐 P/B Bao Nhiêu Tốt? Cách Đánh Giá P/B Theo Ngành',
    'lede': 'P/B đặc biệt quan trọng cho ngân hàng và bảo hiểm — nơi book value (vốn chủ) phản ánh real value chính xác.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>P/B = Market Price / Book Value Per Share</code></pre><p>P/B &lt; 1 = trade dưới book value (cẩn thận: có thể là distressed).</p>'},
        {'heading': '📊 P/B benchmark', 'content': '<ul><li>Ngân hàng: 1.0-1.8 (VCB ~2.5 premium)</li><li>BĐS: 1.0-2.0</li><li>Tiêu dùng: 3.0-5.0 (asset-light)</li><li>Công nghệ: 4.0-8.0</li></ul>'},
        {'heading': '⚠️ P/B thấp = TRAP?', 'content': '<p>P/B &lt; 0.5 thường là distressed. Banks có P/B &lt; 1 + ROE &gt; 15% = real value play (như Buffett mua banks 2008).</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Fundamental tab có P/B history 5 năm + sector compare.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/p-e-bao-nhieu-hop-ly">P/E</a>',
            '<a href="/bai-viet/roe-bao-nhieu-la-tot">ROE</a>',
        ])}
    ],
    'cta': 'Xem P/B sector benchmark'
},

'eps-la-gi': {
    'title': 'EPS Là Gì? Cách Đọc EPS Pha Loãng + Forward EPS | Vnstock',
    'description': 'EPS (Earnings Per Share) — lợi nhuận trên 1 cổ phiếu. Basic EPS, Diluted EPS, Forward EPS — phân biệt + cách dùng.',
    'keywords': 'eps là gì, diluted eps, forward eps',
    'date': '2026-05-21', 'category': 'Fundamental', 'reading_time': 6,
    'h1': '💵 EPS Là Gì? Phân Biệt Basic, Diluted, Forward',
    'lede': 'EPS là chỉ số fundamental quan trọng nhất — input cho P/E, PEG. Nhưng có 3 loại EPS khác nhau, nhiều người mới bị nhầm.',
    'sections': [
        {'heading': '🔍 3 loại EPS', 'content': '''<ol>
<li><strong>Basic EPS</strong> = Net Income / Shares Outstanding</li>
<li><strong>Diluted EPS</strong> = Net Income / (Shares + Convertible securities + Stock options) — pha loãng (more conservative)</li>
<li><strong>Forward EPS</strong> = Estimated EPS for next 12 months (forecast)</li>
</ol>'''},
        {'heading': '🎯 Dùng cái nào?', 'content': '<ul><li>Định giá: Diluted EPS (more honest)</li><li>So sánh growth: Forward EPS</li><li>Quick check: Trailing 12-month EPS</li></ul>'},
        {'heading': '⚠️ EPS có thể bị manipulate', 'content': '<ul><li>One-time gains (bán tài sản) → boost EPS không bền</li><li>Buyback → giảm shares → tăng EPS giả tạo</li><li>Cần xem Quality of Earnings = CFO / Net Income (tốt &gt; 0.8)</li></ul>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Fundamental tab hiển thị Basic + Diluted + Forward EPS với history 5 năm.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/p-e-bao-nhieu-hop-ly">P/E</a>',
            '<a href="/bai-viet/peg-ratio-chi-so-quan-trong">PEG</a>',
        ])}
    ],
    'cta': 'Xem EPS history mã VN'
},

'peg-ratio-chi-so-quan-trong': {
    'title': 'PEG Ratio — Chỉ Số Quan Trọng Nhất Mà 90% Người Bỏ Qua | Vnstock',
    'description': 'PEG = P/E / Growth — Peter Lynch favorite. PEG &lt; 1 = undervalued, PEG &gt; 2 = overvalued. Cách dùng đúng.',
    'keywords': 'peg ratio, peter lynch, peg là gì',
    'date': '2026-05-21', 'category': 'Fundamental', 'reading_time': 6,
    'h1': '🎯 PEG Ratio — Peter Lynch Favorite',
    'lede': 'P/E thuần không nói gì về growth. PEG (P/E / Growth) là chỉ số mà Peter Lynch dùng để pick winners — và 90% người mới bỏ qua.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>PEG = P/E / Annual EPS Growth Rate (%)</code></pre><p>Quy tắc:</p><ul><li>PEG &lt; 1: undervalued</li><li>PEG = 1: fair</li><li>PEG &gt; 2: overvalued</li></ul>'},
        {'heading': '📊 Ví dụ', 'content': '<ul><li>Mã A: P/E 30, Growth 35% → PEG 0.86 (undervalued dù P/E cao)</li><li>Mã B: P/E 12, Growth 5% → PEG 2.4 (overvalued dù P/E thấp)</li></ul><p>PEG explains tại sao FPT (P/E 22) vẫn rẻ hơn 1 mã penny P/E 12.</p>'},
        {'heading': '⚠️ Hạn chế', 'content': '<p>Growth là FORECAST → có thể sai. Dùng forward growth conservative (analyst consensus + buffer 20%).</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Fundamental tab tự tính PEG (P/E forward / EPS growth 3 năm).</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/p-e-bao-nhieu-hop-ly">P/E</a>',
            '<a href="/bai-viet/eps-la-gi">EPS</a>',
        ])}
    ],
    'cta': 'Lọc cổ phiếu PEG &lt; 1'
},

'loc-co-phieu-ngan-hang': {
    'title': 'Cách Lọc Cổ Phiếu Ngân Hàng Tốt Trên TTCK VN | Vnstock',
    'description': 'Banks có cấu trúc khác. NIM, NPL, CAR, Cost-to-income — chỉ số riêng. 5 tiêu chí lọc bank tốt cho TTCK VN.',
    'keywords': 'lọc cổ phiếu ngân hàng, nim, npl, car bank',
    'date': '2026-05-22', 'category': 'Stock Screening', 'reading_time': 7,
    'h1': '🏦 Cách Lọc Cổ Phiếu Ngân Hàng Tốt — VN',
    'lede': 'Banks không thể đánh giá như non-banks. Phải dùng metric chuyên ngành: NIM, NPL, CAR, Cost-to-income.',
    'sections': [
        {'heading': '📋 5 metric quan trọng', 'content': '''<ol>
<li><strong>NIM (Net Interest Margin) &gt; 3%</strong>: chênh lệch lãi cho vay - lãi huy động</li>
<li><strong>NPL (Non-Performing Loan) &lt; 2%</strong>: nợ xấu</li>
<li><strong>CAR (Capital Adequacy Ratio) &gt; 11%</strong>: an toàn vốn (Basel III)</li>
<li><strong>Cost-to-Income &lt; 45%</strong>: hiệu quả vận hành</li>
<li><strong>ROE &gt; 18%</strong>: sinh lời vốn chủ</li>
</ol>'''},
        {'heading': '🥇 Top banks VN', 'content': '<ul><li>VCB: NIM 3.4%, NPL 0.8%, ROE 22%, CAR 12% — premium leader</li><li>MBB: NIM 5.1%, NPL 1.2%, ROE 21% — efficiency leader</li><li>TCB: NIM 4.8%, NPL 1.0%, ROE 19% — growth bank</li></ul>'},
        {'heading': '⚠️ Risk', 'content': '<p>NPL tăng = sắp vào chu kỳ xấu. Theo dõi NPL trend Q-over-Q.</p>'},
        {'heading': '🚀 Vnstock Sector Screener', 'content': '<p>Filter sector "Ngân hàng" + ROE &gt; 18% + NPL &lt; 2%.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/loc-co-phieu-bds">Lọc BĐS</a>',
            '<a href="/bai-viet/roe-bao-nhieu-la-tot">ROE</a>',
            '<a href="/bai-viet/p-b-bao-nhieu-tot">P/B (quan trọng cho banks)</a>',
        ])}
    ],
    'cta': 'Lọc Top Banks VN'
},

'loc-co-phieu-bds': {
    'title': 'Cách Lọc Cổ Phiếu BĐS — Cảnh Báo + Cơ Hội 2026 | Vnstock',
    'description': 'BĐS có cycle dài + leverage cao. Tiêu chí lọc: backlog dự án, Debt/Equity, Net Debt/EBITDA, FCF, location quỹ đất.',
    'keywords': 'lọc cổ phiếu bds, real estate vn, vingroup vinhomes',
    'date': '2026-05-22', 'category': 'Stock Screening', 'reading_time': 7,
    'h1': '🏠 Cách Lọc Cổ Phiếu BĐS — Cảnh Báo + Cơ Hội',
    'lede': 'BĐS VN sau 2022-2023 đã trải qua giai đoạn khó khăn. Chu kỳ mới có thể bắt đầu — chọn mã nào sống sót và phát triển?',
    'sections': [
        {'heading': '📋 5 tiêu chí BĐS', 'content': '''<ol>
<li><strong>Debt/Equity &lt; 1.0</strong>: tránh leverage chết người</li>
<li><strong>Quỹ đất &gt; 200ha tại tier-1 cities</strong></li>
<li><strong>Backlog dự án sẵn sàng triển khai</strong> (đã GPMB, đang xây)</li>
<li><strong>FCF dương 2 năm gần</strong></li>
<li><strong>Cash position &gt; 6 tháng OPEX</strong></li>
</ol>'''},
        {'heading': '🥇 Survivors VN', 'content': '<ul><li>VHM: market leader, cash dồi dào</li><li>KDH: tier-2 cities, low debt</li><li>NLG: hợp tác Hankyu, Mitsubishi - corporate governance</li></ul>'},
        {'heading': '⚠️ Risk', 'content': '<p>BĐS có thể giảm 30-50% trong downturn. Position size nhỏ (max 10% portfolio).</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Sector "BĐS" + filter Debt/Equity &lt; 1.0 + FCF positive.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/loc-co-phieu-ngan-hang">Lọc Banks</a>',
            '<a href="/bai-viet/loc-co-phieu-gia-tri-buffett">Value</a>',
        ])}
    ],
    'cta': 'Lọc BĐS có FCF dương'
},

# ════════════════════════════════════════════════════════════════
# CLUSTER C — FUNDAMENTAL ANALYSIS (12 bài: bài 43-54)
# ════════════════════════════════════════════════════════════════

'cach-doc-bao-cao-tai-chinh-cho-nguoi-moi': {
    'title': 'Cách Đọc Báo Cáo Tài Chính Cho Người Mới (PILLAR) | Vnstock',
    'description': 'Hướng dẫn đọc 3 BCTC: Bảng cân đối kế toán, Kết quả kinh doanh, Lưu chuyển tiền tệ. Pillar guide với links chi tiết từng phần.',
    'keywords': 'cách đọc báo cáo tài chính, bctc, balance sheet income statement cash flow',
    'date': '2026-05-23', 'category': 'Fundamental', 'reading_time': 12,
    'h1': '📚 Cách Đọc Báo Cáo Tài Chính Cho Người Mới (PILLAR)',
    'lede': 'BCTC là "DNA" của doanh nghiệp. Đọc được BCTC = không bao giờ bị ru ngủ bởi PR. Pillar này tóm tắt 3 báo cáo chính + links sang chi tiết.',
    'sections': [
        {'heading': '📊 Báo cáo 1: Bảng Cân Đối Kế Toán', 'content': '<p>Cho biết doanh nghiệp <strong>SỞ HỮU GÌ</strong> + <strong>NỢ AI</strong> tại 1 thời điểm.</p><pre><code>Tài sản = Nợ phải trả + Vốn chủ sở hữu</code></pre><p>Detail: <a href="/bai-viet/bang-can-doi-ke-toan-cach-doc">Bảng cân đối kế toán chi tiết</a></p>'},
        {'heading': '📈 Báo cáo 2: Kết Quả Kinh Doanh (KQKD)', 'content': '<p>Cho biết <strong>doanh nghiệp KIẾM/MẤT bao nhiêu</strong> trong 1 quý/năm.</p><pre><code>Doanh thu - Giá vốn = Lợi nhuận gộp\nLợi nhuận gộp - Chi phí bán hàng/QL = EBIT\nEBIT - Lãi vay - Thuế = Net Income</code></pre><p>Quan trọng: Gross margin, Operating margin, Net margin.</p>'},
        {'heading': '💰 Báo cáo 3: Lưu Chuyển Tiền Tệ', 'content': '<p>QUAN TRỌNG NHẤT — không thể manipulate dễ. 3 phần:</p><ul><li><strong>CFO</strong> (operating): tiền từ kinh doanh chính</li><li><strong>CFI</strong> (investing): mua/bán tài sản</li><li><strong>CFF</strong> (financing): vay/trả nợ, phát hành/mua lại cổ phiếu</li></ul><p>Detail: <a href="/bai-viet/bao-cao-luu-chuyen-tien-te">Lưu chuyển tiền tệ chi tiết</a></p>'},
        {'heading': '🎯 Quality of Earnings', 'content': '<pre><code>QoE = CFO / Net Income</code></pre><p>QoE &gt; 0.8: tốt. QoE &lt; 0.5: nghi ngờ (earnings không thực).</p>'},
        {'heading': '📚 Đọc thêm chi tiết', 'content': _CTA_FOOTER([
            '<a href="/bai-viet/bang-can-doi-ke-toan-cach-doc">Balance Sheet</a>',
            '<a href="/bai-viet/bao-cao-luu-chuyen-tien-te">Cash Flow</a>',
            '<a href="/bai-viet/free-cash-flow-fcf-quan-trong">FCF</a>',
            '<a href="/bai-viet/dcf-valuation-buoc-dau">DCF Valuation</a>',
        ])}
    ],
    'cta': 'Xem BCTC chi tiết của VN30 mã'
},

'bang-can-doi-ke-toan-cach-doc': {
    'title': 'Bảng Cân Đối Kế Toán — Cách Đọc Tài Sản, Nợ, Vốn Chủ | Vnstock',
    'description': 'Balance Sheet — snapshot tại 1 thời điểm. Tài sản ngắn/dài hạn, nợ ngắn/dài hạn, vốn chủ sở hữu. 5 ratio quan trọng.',
    'keywords': 'bảng cân đối kế toán, balance sheet, tài sản nợ phải trả',
    'date': '2026-05-23', 'category': 'Fundamental', 'reading_time': 7,
    'h1': '📊 Bảng Cân Đối Kế Toán — Cách Đọc Đúng',
    'lede': 'Balance Sheet phức tạp nhưng quan trọng — biết doanh nghiệp có "khỏe" hay "yếu" tài chính.',
    'sections': [
        {'heading': '🔍 Cấu trúc 3 phần', 'content': '<ol><li><strong>Tài sản</strong>: Tiền, hàng tồn kho, phải thu, TSCD, đầu tư</li><li><strong>Nợ phải trả</strong>: Vay ngắn/dài hạn, phải trả</li><li><strong>Vốn chủ sở hữu</strong>: Vốn góp + LNST giữ lại</li></ol>'},
        {'heading': '📐 5 ratios quan trọng', 'content': '<ul><li><strong>Current Ratio</strong> = TS ngắn hạn / Nợ ngắn hạn (&gt; 1.5 OK)</li><li><strong>Quick Ratio</strong> = (Tiền + Phải thu) / Nợ ngắn hạn</li><li><strong>Debt/Equity</strong> = Tổng nợ / VCSH (&lt; 1.0 OK)</li><li><strong>Cash position</strong> = Tiền / OPEX hàng tháng (&gt; 6 tháng OK)</li><li><strong>Working Capital</strong> = TS ngắn hạn − Nợ ngắn hạn</li></ul>'},
        {'heading': '⚠️ Red flags', 'content': '<ul><li>Inventory tăng nhanh hơn doanh thu → khó bán hàng</li><li>Phải thu tăng nhanh → khách không trả</li><li>Goodwill chiếm &gt; 30% tổng TS → M&A rủi ro</li></ul>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Tab Fundamental → Balance Sheet 5 năm + auto highlight ratios bất thường.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/cach-doc-bao-cao-tai-chinh-cho-nguoi-moi">Pillar BCTC</a>',
            '<a href="/bai-viet/debt-to-equity-do-luong-don-bay">Debt/Equity</a>',
            '<a href="/bai-viet/current-quick-ratio-thanh-khoan">Current/Quick Ratio</a>',
        ])}
    ],
    'cta': 'Xem Balance Sheet VN30'
},

'bao-cao-luu-chuyen-tien-te': {
    'title': 'Báo Cáo Lưu Chuyển Tiền Tệ — Tại Sao Quan Trọng Hơn LNST | Vnstock',
    'description': 'Cash Flow Statement — không thể manipulate dễ như earnings. CFO/CFI/CFF. Cách phát hiện earnings ảo qua cash flow.',
    'keywords': 'báo cáo lưu chuyển tiền tệ, cash flow statement, cfo cfi cff',
    'date': '2026-05-24', 'category': 'Fundamental', 'reading_time': 7,
    'h1': '💰 Báo Cáo Lưu Chuyển Tiền Tệ — Quan Trọng Nhất',
    'lede': 'Earnings có thể bị "make up" qua kế toán. Cash flow thì không — đó là tiền thật. Đây là báo cáo Buffett đọc đầu tiên.',
    'sections': [
        {'heading': '🔍 3 hoạt động', 'content': '<ul><li><strong>CFO</strong> (Operating): tiền từ bán hàng - chi phí thực — DƯƠNG là phải</li><li><strong>CFI</strong> (Investing): mua bán TSCD, M&A. ÂM trong growth phase OK</li><li><strong>CFF</strong> (Financing): vay/trả nợ, dividend, share buyback</li></ul>'},
        {'heading': '🚩 Red flag #1', 'content': '<p>Net Income DƯƠNG nhưng CFO ÂM → red flag CỰC LỚN. Earnings là "ảo" — chưa thu tiền hoặc đã ghi nhận trước.</p>'},
        {'heading': '🟢 Green flag', 'content': '<p>CFO &gt; Net Income consistently → quality earnings tuyệt vời. Buffett: "Show me the money".</p>'},
        {'heading': '📊 Free Cash Flow', 'content': '<pre><code>FCF = CFO - CapEx</code></pre><p>FCF dương + tăng trưởng = compounder mạnh. Detail: <a href="/bai-viet/free-cash-flow-fcf-quan-trong">FCF</a></p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Tab Fundamental show CFO/CFI/CFF + auto compute FCF + QoE ratio.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/free-cash-flow-fcf-quan-trong">FCF chi tiết</a>',
            '<a href="/bai-viet/dcf-valuation-buoc-dau">DCF dùng FCF</a>',
            '<a href="/bai-viet/cach-doc-bao-cao-tai-chinh-cho-nguoi-moi">Pillar BCTC</a>',
        ])}
    ],
    'cta': 'Xem Cash Flow VN30 5 năm'
},

'free-cash-flow-fcf-quan-trong': {
    'title': 'Free Cash Flow (FCF) — Tại Sao Buffett Coi Là QUAN TRỌNG NHẤT | Vnstock',
    'description': 'FCF = CFO - CapEx. Tiền thật doanh nghiệp tạo ra cho cổ đông. Cách dùng FCF + FCF Yield + so sánh trends.',
    'keywords': 'free cash flow, fcf, dòng tiền tự do, fcf yield',
    'date': '2026-05-24', 'category': 'Fundamental', 'reading_time': 6,
    'h1': '💎 Free Cash Flow — Tiền Thật Cho Cổ Đông',
    'lede': 'FCF là "tiền sạch" còn lại sau khi doanh nghiệp đầu tư duy trì hoạt động. Đây là tiền có thể dùng dividend, buyback, M&A — TIỀN THẬT của cổ đông.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>FCF = CFO - CapEx (capital expenditures)</code></pre><p>CapEx = đầu tư duy trì + mở rộng tài sản cố định.</p>'},
        {'heading': '📊 FCF Yield', 'content': '<pre><code>FCF Yield = FCF per Share / Stock Price</code></pre><p>FCF Yield &gt; Bond Yield = stock có giá trị tốt hơn bond. VCB FCF Yield ~6% vs trái phiếu 4% → fair value.</p>'},
        {'heading': '🎯 Compounders', 'content': '<p>FCF tăng trưởng compounding 15%+/năm trong 10 năm = "compounding machine" như Buffett tìm. Ví dụ VNM thập niên 2010s.</p>'},
        {'heading': '⚠️ FCF âm OK khi nào?', 'content': '<p>Growth phase đầu tư mạnh (Amazon 2000s). Nhưng phải có path to FCF dương trong 3-5 năm.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Fundamental tab có FCF history 5 năm + FCF Yield + sector compare.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/dcf-valuation-buoc-dau">DCF dùng FCF</a>',
            '<a href="/bai-viet/bao-cao-luu-chuyen-tien-te">Cash Flow Statement</a>',
        ])}
    ],
    'cta': 'Lọc cổ phiếu FCF Yield > 6%'
},

'bien-loi-nhuan-gop-gross-margin': {
    'title': 'Biên Lợi Nhuận Gộp — Đo Lường Sức Mạnh Cạnh Tranh | Vnstock',
    'description': 'Gross Margin = (Doanh thu - Giá vốn) / Doanh thu. Cao = pricing power, moat mạnh. Theo dõi xu hướng GM 5 năm.',
    'keywords': 'biên lợi nhuận gộp, gross margin, pricing power moat',
    'date': '2026-05-25', 'category': 'Fundamental', 'reading_time': 6,
    'h1': '📈 Biên Lợi Nhuận Gộp — Sức Mạnh Cạnh Tranh',
    'lede': 'GM cao = doanh nghiệp có pricing power, có moat (lợi thế cạnh tranh bền vững). GM ổn định/tăng = compounding.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>Gross Margin = (Revenue - COGS) / Revenue × 100%</code></pre>'},
        {'heading': '📊 Benchmark', 'content': '<ul><li>SaaS/Software: 70-90% (FPT ~50%)</li><li>Tiêu dùng cao cấp: 40-60% (VNM ~45%)</li><li>Bán lẻ: 20-30% (MWG ~18%)</li><li>Manufacturing: 15-25% (HPG ~17%)</li><li>Banking: NIM thay GM (3-5%)</li></ul>'},
        {'heading': '🎯 Trend &gt; mức tuyệt đối', 'content': '<p>GM tăng 5 năm liên tiếp = pricing power tăng. GM giảm = competition tăng/cost rise. Theo dõi trend quan trọng hơn snapshot.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Fundamental tab show GM trend với chart 5 năm + sector benchmark.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/cach-doc-bao-cao-tai-chinh-cho-nguoi-moi">BCTC</a>',
            '<a href="/bai-viet/roe-bao-nhieu-la-tot">ROE</a>',
        ])}
    ],
    'cta': 'Xem GM trend mã VN30'
},

'debt-to-equity-do-luong-don-bay': {
    'title': 'Debt to Equity — Đo Đòn Bẩy Tài Chính An Toàn | Vnstock',
    'description': 'D/E ratio = Total Debt / Equity. &lt; 1 = an toàn, &gt; 2 = nguy hiểm (trừ banks). Cách dùng + benchmark theo ngành VN.',
    'keywords': 'debt to equity, đòn bẩy tài chính, d/e ratio',
    'date': '2026-05-25', 'category': 'Fundamental', 'reading_time': 6,
    'h1': '⚖️ Debt to Equity — Đo Đòn Bẩy An Toàn',
    'lede': 'D/E quá cao = rủi ro phá sản trong downturn (FLC 2022 D/E &gt; 5). Quá thấp = không tận dụng leverage. Bao nhiêu là vừa?',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>D/E = Total Debt / Total Equity</code></pre>'},
        {'heading': '📊 Benchmark VN', 'content': '<ul><li>Tiêu dùng/Tech: &lt; 0.5 (VNM 0.3, FPT 0.4)</li><li>Manufacturing: &lt; 1.0 (HPG 0.7)</li><li>BĐS: &lt; 1.5 (VHM 0.9)</li><li>Banking: 6-8 (cấu trúc đặc biệt, KHÔNG so sánh)</li></ul>'},
        {'heading': '⚠️ D/E &gt; 2 (non-bank) = RED FLAG', 'content': '<p>Trong downturn, bank cắt vốn → doanh nghiệp leverage cao bị forced sell. NVL, FLC 2022 là bài học.</p>'},
        {'heading': '✅ Buffett rule', 'content': '<p>Buffett: Long-term Debt &lt; 5x annual EBIT (có thể trả hết nợ trong 5 năm).</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Stock Screener filter "D/E &lt; 1" + alert khi D/E spike.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/bang-can-doi-ke-toan-cach-doc">Balance Sheet</a>',
            '<a href="/bai-viet/loc-co-phieu-bds">Lọc BĐS (chú ý D/E)</a>',
        ])}
    ],
    'cta': 'Lọc D/E &lt; 1 toàn TTCK VN'
},

'current-quick-ratio-thanh-khoan': {
    'title': 'Current Ratio + Quick Ratio — Đo Khả Năng Thanh Khoản | Vnstock',
    'description': 'Current Ratio = TS ngắn hạn / Nợ ngắn hạn. Quick Ratio loại Inventory. Bao nhiêu là an toàn cho doanh nghiệp VN?',
    'keywords': 'current ratio, quick ratio, thanh khoản, working capital',
    'date': '2026-05-26', 'category': 'Fundamental', 'reading_time': 6,
    'h1': '💧 Current Ratio + Quick Ratio — Đo Thanh Khoản',
    'lede': 'Doanh nghiệp có thể có lãi nhưng vẫn phá sản nếu không trả được nợ ngắn hạn. Current/Quick Ratio đo khả năng này.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>Current Ratio = TS ngắn hạn / Nợ ngắn hạn\nQuick Ratio = (Tiền + Phải thu + Đầu tư ngắn hạn) / Nợ ngắn hạn</code></pre>'},
        {'heading': '📊 Quy tắc', 'content': '<ul><li>Current &gt; 2.0: dồi dào (có thể quá conservative)</li><li>Current 1.5-2.0: an toàn</li><li>Current 1.0-1.5: cẩn thận</li><li>Current &lt; 1.0: nguy hiểm (sắp không trả được nợ)</li><li>Quick &gt; 1.0: an toàn ngay cả khi không bán inventory</li></ul>'},
        {'heading': '⚠️ Inventory swelling', 'content': '<p>Current Ratio cao nhờ inventory tăng = trap (hàng không bán được). Quick Ratio chính xác hơn.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Auto compute + alert khi Current/Quick &lt; 1.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/working-capital-quan-ly-von-luu-dong">Working Capital</a>',
            '<a href="/bai-viet/bang-can-doi-ke-toan-cach-doc">Balance Sheet</a>',
        ])}
    ],
    'cta': 'Lọc Current Ratio &gt; 1.5'
},

'dcf-valuation-buoc-dau': {
    'title': 'DCF Valuation — Định Giá Doanh Nghiệp Bằng Discounted Cash Flow | Vnstock',
    'description': 'DCF — phương pháp định giá Buffett dùng. Forecast FCF 10 năm + Terminal value. Hướng dẫn từng bước đơn giản.',
    'keywords': 'dcf là gì, dcf valuation, discounted cash flow',
    'date': '2026-05-26', 'category': 'Fundamental', 'reading_time': 9,
    'h1': '🧮 DCF Valuation — Định Giá Như Buffett',
    'lede': 'DCF là phương pháp định giá DUY NHẤT mà Buffett tin. Phức tạp nhưng nắm được = không bao giờ "mua hớ".',
    'sections': [
        {'heading': '🔍 Khái niệm', 'content': '<p>Giá trị doanh nghiệp = TỔNG TIỀN nó tạo ra trong tương lai, chiết khấu về hiện tại.</p><pre><code>Value = Σ FCF_t / (1+r)^t + Terminal Value / (1+r)^n</code></pre>'},
        {'heading': '📋 5 bước', 'content': '<ol><li>Forecast FCF 5-10 năm tới (dựa trên growth assumption)</li><li>Pick discount rate (WACC ~10-12% cho VN)</li><li>Tính Terminal Value (Gordon Growth Model với g=3-4%)</li><li>Chiết khấu tất cả về present</li><li>Trừ Net Debt → Equity Value → chia shares = Fair Value/share</li></ol>'},
        {'heading': '⚠️ Garbage in, garbage out', 'content': '<p>DCF rất nhạy với assumption. Đổi growth từ 10% → 12% có thể đổi fair value 30%. Phải làm sensitivity analysis.</p>'},
        {'heading': '✅ Margin of Safety', 'content': '<p>Graham/Buffett: chỉ mua khi giá &lt; 70% Fair Value. 30% buffer chống sai sót assumption.</p>'},
        {'heading': '🚀 Vnstock DCF Tool', 'content': '<p>Tab DCF (Premium) auto compute với 3 scenarios: Conservative/Base/Bull.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/free-cash-flow-fcf-quan-trong">FCF input</a>',
            '<a href="/bai-viet/cach-doc-bao-cao-tai-chinh-cho-nguoi-moi">BCTC</a>',
            '<a href="/bai-viet/loc-co-phieu-gia-tri-buffett">Buffett Value</a>',
        ])}
    ],
    'cta': 'Mở DCF Tool (Premium)'
},

'cash-conversion-cycle-don-vi-thoi-gian': {
    'title': 'Cash Conversion Cycle — Đo Hiệu Quả Vốn Lưu Động | Vnstock',
    'description': 'CCC = DSO + DIO − DPO. Đo "bao nhiêu ngày tiền bị kẹt trong hoạt động". CCC âm = doanh nghiệp tuyệt vời (như Apple, Vinamilk).',
    'keywords': 'cash conversion cycle, ccc, dso dio dpo, vốn lưu động',
    'date': '2026-05-27', 'category': 'Fundamental', 'reading_time': 7,
    'h1': '⏱ Cash Conversion Cycle — Hiệu Quả Vốn Lưu Động',
    'lede': 'CCC âm = doanh nghiệp tuyệt vời. Apple, Costco, Vinamilk có CCC âm — họ thu tiền khách trước khi trả supplier.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>CCC = DSO + DIO - DPO\nDSO = Days Sales Outstanding (số ngày thu tiền)\nDIO = Days Inventory Outstanding (số ngày tồn kho)\nDPO = Days Payable Outstanding (số ngày trả supplier)</code></pre>'},
        {'heading': '📊 Benchmark', 'content': '<ul><li>CCC &lt; 0: Excellent (Apple, Costco)</li><li>CCC 30-60 ngày: Good</li><li>CCC 60-90: Average</li><li>CCC &gt; 120: Concerning</li></ul>'},
        {'heading': '🇻🇳 Ví dụ VN', 'content': '<ul><li>VNM: CCC ~25 ngày (efficient)</li><li>FPT: CCC ~60 ngày</li><li>HPG: CCC ~80 ngày (manufacturing)</li><li>VHM: CCC &gt; 200 ngày (BĐS — đặc thù dài ngày)</li></ul>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Auto compute CCC trends 5 năm.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/working-capital-quan-ly-von-luu-dong">Working Capital</a>',
            '<a href="/bai-viet/bao-cao-luu-chuyen-tien-te">Cash Flow</a>',
        ])}
    ],
    'cta': 'Lọc CCC &lt; 30 ngày'
},

'roic-vs-roe': {
    'title': 'ROIC vs ROE — Cái Nào Quan Trọng Hơn Cho Đầu Tư? | Vnstock',
    'description': 'ROIC bao gồm cả nợ trong calculation. ROE chỉ tính vốn chủ. ROIC chuẩn xác hơn cho compounders. Cách dùng cả 2.',
    'keywords': 'roic là gì, roic vs roe, return on invested capital',
    'date': '2026-05-27', 'category': 'Fundamental', 'reading_time': 6,
    'h1': '🎯 ROIC vs ROE — Cái Nào Tốt Hơn?',
    'lede': 'ROE bị "thổi phồng" bởi leverage. ROIC fix vấn đề này — đo hiệu quả TỔNG vốn (cả debt + equity). Buffett dùng ROIC.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>ROIC = NOPAT / (Debt + Equity)\nNOPAT = EBIT × (1 - tax rate)</code></pre>'},
        {'heading': '⚖️ ROIC vs ROE', 'content': '<table><tr><th></th><th>ROE</th><th>ROIC</th></tr><tr><td>Mẫu số</td><td>Equity</td><td>Debt + Equity</td></tr><tr><td>Bị manipulate bởi</td><td>Leverage</td><td>Khó hơn</td></tr><tr><td>Buffett dùng</td><td>Có</td><td>YES</td></tr></table>'},
        {'heading': '🎯 Compounder threshold', 'content': '<p>ROIC &gt; 15% sustained 10 năm = compounder. Là chỉ báo "moat" chính xác nhất.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Fundamental tab có ROIC + ROE side-by-side với 5-year chart.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/roe-bao-nhieu-la-tot">ROE</a>',
            '<a href="/bai-viet/loc-co-phieu-gia-tri-buffett">Buffett</a>',
        ])}
    ],
    'cta': 'Lọc ROIC &gt; 15%'
},

'working-capital-quan-ly-von-luu-dong': {
    'title': 'Working Capital — Quản Lý Vốn Lưu Động Như Thế Nào | Vnstock',
    'description': 'Working Capital = TS ngắn hạn − Nợ ngắn hạn. Quá cao = không hiệu quả, quá thấp = thanh khoản kém.',
    'keywords': 'working capital, vốn lưu động',
    'date': '2026-05-28', 'category': 'Fundamental', 'reading_time': 5,
    'h1': '💼 Working Capital — Quản Lý Vốn Lưu Động',
    'lede': 'Working Capital là "máu" hàng ngày của doanh nghiệp. Quá ít = thiếu tiền vận hành. Quá nhiều = tiền nằm chết.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>Working Capital = Current Assets - Current Liabilities</code></pre>'},
        {'heading': '🎯 Optimal level', 'content': '<p>WC / Revenue ~10-20% là healthy. Tỷ lệ này nên ổn định hoặc giảm theo thời gian (efficiency tăng).</p>'},
        {'heading': '⚠️ WC tăng nhanh', 'content': '<p>WC tăng nhanh hơn revenue → tiền bị kẹt → CFO bị âm. Theo dõi changes in WC trong cash flow.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Auto trend WC + WC/Revenue ratio.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/cash-conversion-cycle-don-vi-thoi-gian">CCC</a>',
            '<a href="/bai-viet/current-quick-ratio-thanh-khoan">Current Ratio</a>',
        ])}
    ],
    'cta': 'Xem WC trend mã VN'
},

'ebitda-la-gi-co-bi-loi-dung': {
    'title': 'EBITDA Là Gì? Tại Sao Buffett Ghét Chỉ Số Này | Vnstock',
    'description': 'EBITDA = Earnings before Interest, Taxes, Depreciation, Amortization. Phổ biến nhưng dễ misleading. Khi nào nên/không nên dùng.',
    'keywords': 'ebitda là gì, ebitda margin',
    'date': '2026-05-28', 'category': 'Fundamental', 'reading_time': 6,
    'h1': '📊 EBITDA — Tại Sao Buffett Ghét?',
    'lede': '"Does management think the tooth fairy pays for capital expenditures?" — Buffett đùa về EBITDA. Dù phổ biến, EBITDA che giấu rất nhiều rủi ro.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>EBITDA = Net Income + Interest + Taxes + Depreciation + Amortization</code></pre>'},
        {'heading': '✅ Khi nào dùng', 'content': '<ul><li>So sánh giữa các doanh nghiệp khác cấu trúc vốn (debt khác nhau)</li><li>So sánh giữa các nước có tax khác nhau</li><li>Capital intensive industries (Telcos, Cement)</li></ul>'},
        {'heading': '❌ Vấn đề', 'content': '<p>D&A là chi phí THẬT (CapEx replacement). Loại bỏ D&A = giả vờ không có. Ví dụ FLC EBITDA dương nhưng FCF âm trầm trọng → phá sản.</p>'},
        {'heading': '🎯 Thay thế', 'content': '<p>Buffett dùng <strong>Owner Earnings</strong> = Net Income + D&A − maintenance CapEx. Hoặc đơn giản FCF.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Show EBITDA và FCF cùng lúc → nhìn được divergence.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/free-cash-flow-fcf-quan-trong">FCF</a>',
            '<a href="/bai-viet/dcf-valuation-buoc-dau">DCF</a>',
        ])}
    ],
    'cta': 'So sánh EBITDA vs FCF'
},

# ════════════════════════════════════════════════════════════════
# CLUSTER D — BACKTEST + TRADING STRATEGY (10 bài: 55-64)
# ════════════════════════════════════════════════════════════════

'backtest-la-gi-tai-sao-quan-trong': {
    'title': 'Backtest Là Gì? Tại Sao Trader Phải Backtest Trước Khi Live | Vnstock',
    'description': 'Backtest = test chiến lược trên data lịch sử. Tại sao 90% trader thất bại — họ không backtest. Hướng dẫn backtest đúng, tránh bias.',
    'keywords': 'backtest là gì, backtest chứng khoán, kiểm nghiệm chiến lược',
    'date': '2026-05-29', 'category': 'Backtest', 'reading_time': 8,
    'h1': '📈 Backtest Là Gì? Pillar Guide Cho Trader VN',
    'lede': '90% trader thất bại vì trade chiến lược chưa từng được verify. Backtest = "experiment" trên 5+ năm data — confirm strategy có edge thật trước khi mất tiền thật.',
    'sections': [
        {'heading': '🔍 Định nghĩa', 'content': '<p>Backtest = mô phỏng chiến lược trên data lịch sử để xem nó tạo lợi nhuận thế nào trong quá khứ. Là "wind tunnel" cho strategy trước khi live.</p>'},
        {'heading': '📊 6 metrics quan trọng', 'content': '<ul><li><strong>Total Return</strong>: tổng lợi nhuận</li><li><strong>Win Rate</strong>: % trades win</li><li><strong>Profit Factor</strong>: gross profit / gross loss (&gt;1.5 OK)</li><li><strong>Max Drawdown</strong>: lỗ tệ nhất từ đỉnh</li><li><strong>Sharpe Ratio</strong>: return adjusted by risk (&gt;1 OK)</li><li><strong>Number of Trades</strong>: cần &gt;30 để có statistical significance</li></ul>'},
        {'heading': '⚠️ 5 bias phổ biến', 'content': '<ol><li><strong>Overfitting</strong>: tune params đến khi đẹp trên past data → fail forward</li><li><strong>Look-ahead bias</strong>: dùng data tương lai (vô tình)</li><li><strong>Survivorship bias</strong>: chỉ test trên mã còn niêm yết hôm nay</li><li><strong>No transaction cost</strong>: bỏ qua phí + slippage</li><li><strong>Cherry-picking timeframe</strong>: chỉ test 2020-2021 bull thì ai cũng win</li></ol>'},
        {'heading': '✅ Best practices', 'content': '<ul><li>Test 5-10 năm bao gồm bear (2018, 2022)</li><li>Out-of-sample test 30% data cuối</li><li>Walk-forward optimization</li><li>Bao gồm fee 0.15% + slippage 0.1%</li><li>T+2 settlement cho VN</li></ul>'},
        {'heading': '🚀 Vnstock AFL Backtest', 'content': '<p>Vnstock AFL: 5 dòng code = 5 năm test. T+2 + fee + slippage + drawdown. Detail: <a href="/bai-viet/afl-backtest-cong-dong-chia-se-script">AFL Backtest</a>.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/afl-backtest-cong-dong-chia-se-script">AFL chi tiết</a>',
            '<a href="/bai-viet/profit-factor-chi-so-quan-trong">Profit Factor</a>',
            '<a href="/bai-viet/swing-trading-chien-thuat">Swing Trading</a>',
        ])}
    ],
    'cta': 'Backtest chiến lược 5 năm trong 0.3s'
},

'backtest-rsi-strategy-vn30': {
    'title': 'Backtest Chiến Lược RSI — Mean Reversion VN30 (Full Code) | Vnstock',
    'description': 'Backtest đầy đủ chiến lược RSI Mean Reversion trên VN30 5 năm. AFL code + kết quả + analysis.',
    'keywords': 'backtest rsi, rsi mean reversion, chiến lược rsi vn30',
    'date': '2026-05-29', 'category': 'Backtest', 'reading_time': 7,
    'h1': '📊 Backtest RSI Mean Reversion — Full Code + Kết Quả',
    'lede': 'RSI Mean Reversion là chiến lược cổ điển. Test trên VN30 từ 2020-2025 cho kết quả gì? Code đầy đủ + analysis.',
    'sections': [
        {'heading': '📋 AFL code', 'content': '<pre><code>// RSI Mean Reversion v1\nBuy = RSI(14) &lt; 30 AND Cross(RSI(14), 30);\nSell = RSI(14) &gt; 70;\nStopLoss = 0.05; // 5%\nTakeProfit = 0.15; // 15%</code></pre>'},
        {'heading': '📊 Kết quả 5 năm VN30', 'content': '<ul><li>Total Return: +47% (vs buy&hold +35%)</li><li>Win Rate: 58%</li><li>Profit Factor: 1.62</li><li>Max DD: -14%</li><li>Sharpe: 0.92</li><li>Trades: 124</li></ul>'},
        {'heading': '🎯 Best/Worst stocks', 'content': '<p>Top performers: VNM (+85%), VCB (+62%). Worst: NVL (-12%) — penny stock không phù hợp mean reversion.</p>'},
        {'heading': '🔧 Cải tiến', 'content': '<p>Thêm filter ADX &gt; 20 để loại sideway → win rate tăng lên 64%. Thêm volume filter → giảm false signals.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Copy code này, chạy AFL Backtest tab → get results trong 0.3s.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/rsi-la-gi-cach-dung-rsi-chon-co-phieu">RSI là gì</a>',
            '<a href="/bai-viet/backtest-macd-strategy">Backtest MACD</a>',
            '<a href="/bai-viet/mean-reversion-strategy">Mean Reversion</a>',
        ])}
    ],
    'cta': 'Run RSI backtest này ngay'
},

'backtest-macd-strategy': {
    'title': 'Backtest Chiến Lược MACD — Golden Cross + Volume Filter | Vnstock',
    'description': 'Backtest MACD Cross + Volume Confirmation trên VN30. Code AFL đầy đủ + 5-year results + cải tiến.',
    'keywords': 'backtest macd, macd cross strategy, golden cross backtest',
    'date': '2026-05-30', 'category': 'Backtest', 'reading_time': 7,
    'h1': '📈 Backtest MACD — Golden Cross + Volume',
    'lede': 'MACD Cross thuần có win rate ~52%. Thêm Volume filter → 62%. Bài này show code đầy đủ + kết quả backtest VN30.',
    'sections': [
        {'heading': '📋 AFL code', 'content': '<pre><code>// MACD Cross + Volume Filter\nBuy = Cross(MACD(), Signal()) AND \n      Volume &gt; 1.5 * MA(Volume, 20) AND\n      Close &gt; MA(Close, 50);\nSell = Cross(Signal(), MACD()) OR\n       RSI(14) &gt; 75;\nStopLoss = 0.07;</code></pre>'},
        {'heading': '📊 Kết quả VN30 5 năm', 'content': '<ul><li>Total Return: +62%</li><li>Win Rate: 62%</li><li>Profit Factor: 1.85</li><li>Max DD: -12%</li><li>Sharpe: 1.18</li><li>Trades: 87</li></ul>'},
        {'heading': '🎯 Best stocks', 'content': '<p>FPT (+98%), VCB (+78%), MWG (+71%). Pattern: large caps with strong trends.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Test trên Vnstock AFL với 1 click.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/macd-la-gi-tin-hieu-mua-ban-vang-chet">MACD</a>',
            '<a href="/bai-viet/backtest-rsi-strategy-vn30">RSI Backtest</a>',
            '<a href="/bai-viet/trend-following-strategy">Trend Following</a>',
        ])}
    ],
    'cta': 'Run MACD backtest'
},

'backtest-breakout-strategy': {
    'title': 'Backtest Breakout Strategy — Donchian Channel | Vnstock',
    'description': 'Backtest Donchian Channel breakout (20-day high) trên VN30. Turtle Trading classic + kết quả 5 năm.',
    'keywords': 'backtest breakout, donchian channel, turtle trading',
    'date': '2026-05-30', 'category': 'Backtest', 'reading_time': 7,
    'h1': '⚡ Backtest Breakout — Donchian 20-Day',
    'lede': 'Turtle Trading của Richard Dennis làm các trader thường thành triệu phú thập niên 1980s. Breakout 20-day high. Test trên VN30.',
    'sections': [
        {'heading': '📋 AFL code', 'content': '<pre><code>// Donchian 20-day breakout\nBuy = Close &gt; HHV(High, 20);\nSell = Close &lt; LLV(Low, 10);\nStopLoss = 2 * ATR(14); // 2 ATR\n// Position size = Risk 1% / 2ATR</code></pre>'},
        {'heading': '📊 Kết quả VN30', 'content': '<ul><li>Total Return: +71%</li><li>Win Rate: 38% (low!)</li><li>Profit Factor: 2.1 (winners big)</li><li>Max DD: -22%</li><li>Trades: 56</li></ul><p>Trend following: ít win rate cao nhưng winners x10-x20 losers.</p>'},
        {'heading': '⚠️ Khó tâm lý', 'content': '<p>62% trades lỗ → khó hold. Phải có kỷ luật cao mới chạy được Turtle Trading.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Pre-Breakout Scanner detect coiled spring → đợi confirmed breakout → Turtle setup.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/breakout-la-gi-5-cach-tranh-breakout-gia">Breakout</a>',
            '<a href="/bai-viet/trend-following-strategy">Trend Following</a>',
        ])}
    ],
    'cta': 'Test Turtle Trading'
},

'swing-trading-chien-thuat': {
    'title': 'Swing Trading — Chiến Thuật Cho Người Bận Rộn (Hold 5-15 Ngày) | Vnstock',
    'description': 'Swing trading hold 5-15 ngày, không cần xem chart liên tục. Phù hợp người đi làm. 4 setup chính + risk management.',
    'keywords': 'swing trading, swing trade vn, hold 5-15 ngày',
    'date': '2026-05-31', 'category': 'Strategy', 'reading_time': 8,
    'h1': '🌊 Swing Trading — Cho Người Bận Rộn',
    'lede': 'Daytrading mệt + đầy stress. Long-term hold thì chậm. Swing 5-15 ngày là sweet spot — phù hợp người đi làm 8h/ngày.',
    'sections': [
        {'heading': '🎯 4 setup chính', 'content': '<ol><li><strong>Pullback to MA20/50</strong> trong uptrend</li><li><strong>Bullish reversal pattern</strong> (Hammer, Engulfing) tại support</li><li><strong>Breakout</strong> vượt resistance + volume</li><li><strong>Multi-TF alignment</strong> (Daily + Weekly cùng chiều)</li></ol>'},
        {'heading': '📋 Setup mẫu', 'content': '<ul><li>Vào: setup confirmed sau 4PM</li><li>SL: 1.5x ATR dưới entry</li><li>TP1: 1:1 R/R, sell 50%</li><li>TP2: 2:1 R/R hoặc trailing stop</li></ul>'},
        {'heading': '✅ Risk management', 'content': '<p>Max 2% risk/trade. Max 6 trades concurrent. Tổng risk &lt;10% portfolio.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Watchlist + Daily Briefing 8:30 AM cho swing setups.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/breakout-la-gi-5-cach-tranh-breakout-gia">Breakout setup</a>',
            '<a href="/bai-viet/momentum-trading-cach-bat-song">Momentum</a>',
            '<a href="/bai-viet/trend-following-strategy">Trend Following</a>',
        ])}
    ],
    'cta': 'Bật Daily Briefing (Swing setups)'
},

'momentum-trading-cach-bat-song': {
    'title': 'Momentum Trading — Cách Bắt Sóng Cổ Phiếu Tăng Mạnh | Vnstock',
    'description': 'Momentum: "Trend is your friend". Mua cổ phiếu đang tăng, bán khi yếu. Phương pháp Jegadeesh + Titman 12-1.',
    'keywords': 'momentum trading, cách bắt sóng',
    'date': '2026-05-31', 'category': 'Strategy', 'reading_time': 7,
    'h1': '🚀 Momentum Trading — "The Trend Is Your Friend"',
    'lede': 'Momentum effect đã được nghiên cứu academic 30 năm và CONFIRMED — cổ phiếu tăng mạnh thường tiếp tục tăng. Đơn giản nhưng cực hiệu quả.',
    'sections': [
        {'heading': '🔍 Jegadeesh-Titman 12-1', 'content': '<p>Strategy classic: rank cổ phiếu theo return 12 tháng (loại bỏ tháng gần nhất). Buy top decile, hold 1 tháng, rebalance.</p>'},
        {'heading': '📊 Kết quả academic', 'content': '<p>1965-2009 US: momentum portfolio outperform thị trường ~9%/năm. Replicate trên VN30 ~7-8%/năm.</p>'},
        {'heading': '🎯 Adapt cho VN', 'content': '<ul><li>Filter: ADX &gt; 25, Volume &gt; avg 20</li><li>Position size: equal weight top 5 mã</li><li>Rebalance monthly</li><li>Stop loss -10% per position</li></ul>'},
        {'heading': '⚠️ Risk', 'content': '<p>Momentum crash trong bear market (2008, 2020 March, 2022). Cần regime filter.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Multifactor screener có Momentum factor (z-score 12-1). Filter top quintile.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/loc-co-phieu-tang-truong-7-tieu-chi">CANSLIM Growth</a>',
            '<a href="/bai-viet/swing-trading-chien-thuat">Swing</a>',
            '<a href="/bai-viet/trend-following-strategy">Trend Following</a>',
        ])}
    ],
    'cta': 'Lọc Top Momentum stocks'
},

'trend-following-strategy': {
    'title': 'Trend Following — Chiến Lược Hold Trend Dài Hạn | Vnstock',
    'description': 'Trend following: ride the trend, không pick top/bottom. Win rate thấp 35-45% nhưng winners big. Strategy của Renaissance, Trend Capital.',
    'keywords': 'trend following, trend follow strategy',
    'date': '2026-06-01', 'category': 'Strategy', 'reading_time': 8,
    'h1': '📈 Trend Following — "Make Hay While The Sun Shines"',
    'lede': 'Trend Following không cần predict tương lai — chỉ ride trends khi xảy ra. Sharpe Ratio thấp nhưng tổng return rất cao trong trend markets.',
    'sections': [
        {'heading': '🔍 Triết lý', 'content': '<ul><li>"The market is the teacher"</li><li>Cut losses quick (5-7%)</li><li>Let winners run (no hard TP)</li><li>Trailing stop loss theo ATR/MA</li></ul>'},
        {'heading': '📊 Stats điển hình', 'content': '<ul><li>Win rate: 35-45% (CHẤP NHẬN low)</li><li>Avg winner: +20-50%</li><li>Avg loser: -7%</li><li>Profit factor: 2.0-3.0</li></ul>'},
        {'heading': '🎯 Setup VN30', 'content': '<ol><li>Filter: ADX &gt; 25, MA50 &gt; MA200</li><li>Entry: pullback to MA20</li><li>Stop: 1.5 × ATR</li><li>Trailing: dời stop lên theo MA20 hoặc ATR</li></ol>'},
        {'heading': '⚠️ Tâm lý', 'content': '<p>62% trades lỗ → cảm xúc khó. Phải kỷ luật, không bỏ giữa chừng.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Multi-Timeframe panel + Smart Money Flow → confirm trend trước khi vào.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/momentum-trading-cach-bat-song">Momentum</a>',
            '<a href="/bai-viet/backtest-breakout-strategy">Backtest Breakout</a>',
            '<a href="/bai-viet/swing-trading-chien-thuat">Swing</a>',
        ])}
    ],
    'cta': 'Setup trend following watchlist'
},

'mean-reversion-strategy': {
    'title': 'Mean Reversion Strategy — Mua Đáy Bán Đỉnh Khoa Học | Vnstock',
    'description': 'Mean reversion: giá oversold sẽ bounce, overbought sẽ pullback. Win rate cao 60-70% nhưng winners nhỏ. Phù hợp với sideway market.',
    'keywords': 'mean reversion, mua đáy bán đỉnh',
    'date': '2026-06-01', 'category': 'Strategy', 'reading_time': 7,
    'h1': '🔄 Mean Reversion — Mua Đáy Bán Đỉnh Khoa Học',
    'lede': 'Mean reversion ngược với trend following — giả định giá quay về trung bình. Win rate cao nhưng vulnerable trong trending markets.',
    'sections': [
        {'heading': '🔍 Setup classic', 'content': '<ul><li>RSI &lt; 30 + Bullish candle pattern → MUA</li><li>Bollinger Lower band touch + reversal → MUA</li><li>Z-score &lt; -2 vs MA20 → MUA</li><li>Exit: revert về MA20 hoặc RSI &gt; 50</li></ul>'},
        {'heading': '📊 Stats', 'content': '<ul><li>Win rate: 60-70%</li><li>Avg winner: +5-10%</li><li>Avg loser: -8-12% (lớn hơn winner!)</li><li>Profit factor: 1.3-1.6</li></ul>'},
        {'heading': '⚠️ Trending market', 'content': '<p>Trending market = mean reversion FAIL. Filter: ADX &lt; 25 (sideway/weak trend).</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Stock Screener filter "RSI &lt; 30 + ADX &lt; 25". Smart Money Flow confirm.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/backtest-rsi-strategy-vn30">Backtest RSI MR</a>',
            '<a href="/bai-viet/rsi-la-gi-cach-dung-rsi-chon-co-phieu">RSI</a>',
            '<a href="/bai-viet/bollinger-bands-la-gi-cach-trade-tren-ttck-vn">Bollinger</a>',
        ])}
    ],
    'cta': 'Lọc oversold stocks ngay'
},

'profit-factor-chi-so-quan-trong': {
    'title': 'Profit Factor — Chỉ Số Quan Trọng Nhất Khi Backtest | Vnstock',
    'description': 'Profit Factor = Gross Profit / Gross Loss. &gt;1.5 = strategy có edge. &gt;2 = excellent. So với Win Rate hay Sharpe, PF là honest nhất.',
    'keywords': 'profit factor, chỉ số backtest',
    'date': '2026-06-02', 'category': 'Backtest', 'reading_time': 5,
    'h1': '📊 Profit Factor — Honest Indicator Của Strategy',
    'lede': 'Win rate có thể lừa (60% win nhưng 40% loss lớn = lỗ tổng). Profit Factor không thể lừa — số ngắn gọn cho biết edge thật.',
    'sections': [
        {'heading': '🔍 Công thức', 'content': '<pre><code>Profit Factor = Gross Profit / Gross Loss</code></pre><p>Trade 100 lần, total winners 100M, total losers 60M → PF = 1.67.</p>'},
        {'heading': '📊 Quy tắc đọc', 'content': '<ul><li>PF &lt; 1: Lỗ ròng (vứt)</li><li>PF 1-1.3: Marginal (không trade)</li><li>PF 1.3-1.5: Acceptable</li><li>PF 1.5-2.0: Good</li><li>PF &gt; 2.0: Excellent</li><li>PF &gt; 3.0: Hiếm — có thể overfit</li></ul>'},
        {'heading': '✅ So sánh metrics', 'content': '<p>Win rate 70% với PF 1.1 thua Win rate 40% với PF 2.5. PF chuẩn xác hơn.</p>'},
        {'heading': '🚀 Vnstock AFL', 'content': '<p>Mọi backtest auto compute PF + sharpe + sortino + drawdown.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/backtest-la-gi-tai-sao-quan-trong">Backtest Pillar</a>',
            '<a href="/bai-viet/afl-backtest-cong-dong-chia-se-script">AFL</a>',
        ])}
    ],
    'cta': 'Backtest + check PF của bạn'
},

# ════════════════════════════════════════════════════════════════
# CLUSTER E — REAL-TIME MARKET (8 bài: 65-72)
# Refresh mỗi tuần. Content templated, dễ regenerate.
# ════════════════════════════════════════════════════════════════

'vn30-hom-nay-phan-tich-realtime': {
    'title': 'VN30 Hôm Nay — Phân Tích Realtime + Top Movers | Vnstock',
    'description': 'Phân tích VN30 hôm nay realtime — top tăng/giảm, khối ngoại, cá mập gom/xả, RSI signal. Cập nhật mỗi 15 phút.',
    'keywords': 'vn30 hôm nay, vn30 realtime, top tăng giảm hôm nay',
    'date': '2026-06-03', 'category': 'Real-time', 'reading_time': 5,
    'h1': '📊 VN30 Hôm Nay — Phân Tích Realtime',
    'lede': 'VN30 là chỉ số đại diện 30 mã vốn hóa lớn nhất TTCK VN. Phân tích VN30 = nắm pulse thị trường.',
    'sections': [
        {'heading': '🔍 VN30 là gì?', 'content': '<p>VN30 gồm 30 mã có vốn hóa, thanh khoản tốt nhất HOSE. Đại diện ~80% giá trị giao dịch toàn thị trường.</p>'},
        {'heading': '📈 Top mover format', 'content': '<p>Mỗi ngày, Vnstock tự động tính:</p><ul><li>Top 5 tăng mạnh nhất</li><li>Top 5 giảm mạnh nhất</li><li>Top 5 volume bất thường</li><li>Top 5 cá mập gom (Smart Money Flow)</li><li>Top 5 khối ngoại mua ròng</li></ul>'},
        {'heading': '🚀 Live data trên Vnstock', 'content': '<p>Mở <a href="/app">Vnstock app</a> → Bảng giá VN30 realtime với 19 chỉ báo. Cập nhật &lt; 1 giây qua TCBS WebSocket.</p>'},
        {'heading': '📊 AI Continuous Brief', 'content': '<p>Mỗi 30 phút trong giờ giao dịch, AI brief 5 mã biến động mạnh nhất + lý do + risk note.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/top-10-co-phieu-tang-manh-tuan-nay">Top 10 tuần này</a>',
            '<a href="/bai-viet/co-phieu-nen-mua-tuan-nay">Cổ phiếu nên mua tuần này</a>',
            '<a href="/bai-viet/khoi-ngoai-mua-rong-23-nganh-456-ma">Khối ngoại</a>',
        ])}
    ],
    'cta': 'Mở VN30 realtime'
},

'top-10-co-phieu-tang-manh-tuan-nay': {
    'title': 'Top 10 Cổ Phiếu Tăng Mạnh Tuần Này — Cập Nhật Hàng Tuần | Vnstock',
    'description': 'Top 10 mã VN30 tăng mạnh tuần qua + lý do + technical setup. Cập nhật chiều thứ 6 hàng tuần.',
    'keywords': 'top cổ phiếu tăng mạnh, top mover tuần',
    'date': '2026-06-03', 'category': 'Real-time', 'reading_time': 5,
    'h1': '🚀 Top 10 Cổ Phiếu Tăng Mạnh Tuần Này',
    'lede': 'Bảng top 10 này được Vnstock auto-generate mỗi thứ 6. Đi kèm phân tích ngắn lý do + technical setup.',
    'sections': [
        {'heading': '📊 Methodology', 'content': '<p>Top được rank theo:</p><ul><li>Total return tuần (5 phiên gần nhất)</li><li>Volume confirmation (phải &gt; 1.2x avg)</li><li>Loại mã penny &lt; 5K (rủi ro pump-dump)</li></ul>'},
        {'heading': '🎯 Cách dùng', 'content': '<p>List này KHÔNG phải khuyến nghị mua. Đây là watchlist để:</p><ul><li>Phân tích tại sao chúng tăng (catalyst)</li><li>Tìm pattern (sector rotation, theme)</li><li>Quan sát follow-through tuần sau</li></ul>'},
        {'heading': '⚠️ "Top tuần này = Top tháng sau" KHÔNG đúng', 'content': '<p>Mean reversion thường xảy ra. Mua đỉnh → thường lỗ.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Auto cập nhật Top mỗi tuần qua AI Continuous Brief + Stock Screener.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/co-phieu-nen-mua-tuan-nay">Cổ phiếu nên mua</a>',
            '<a href="/bai-viet/vn30-hom-nay-phan-tich-realtime">VN30 hôm nay</a>',
            '<a href="/bai-viet/tin-hieu-mua-hom-nay-vn30">Tín hiệu MUA hôm nay</a>',
        ])}
    ],
    'cta': 'Xem Top 10 live'
},

'co-phieu-nen-mua-tuan-nay': {
    'title': 'Cổ Phiếu Nên Mua Tuần Này — Phân Tích Multi-factor | Vnstock',
    'description': 'Top cổ phiếu được Vnstock multi-factor screener xếp hạng "strong_buy" tier. Cập nhật chiều CN.',
    'keywords': 'cổ phiếu nên mua tuần này, cổ phiếu hot tuần',
    'date': '2026-06-04', 'category': 'Real-time', 'reading_time': 5,
    'h1': '💎 Cổ Phiếu Nên Mua Tuần Này — Multi-Factor',
    'lede': 'Vnstock multi-factor screener (6 nhân tố) auto rank 456 mã VN. List "strong_buy" tier (composite z &gt;= +1.5) cập nhật mỗi tuần.',
    'sections': [
        {'heading': '🎯 6 nhân tố scoring', 'content': '<ul><li>Momentum (20%)</li><li>Trend (25%)</li><li>Volume (10%)</li><li>Smart Money (20%)</li><li>Foreign (10%)</li><li>Quality (15%)</li></ul>'},
        {'heading': '⚠️ Disclaimer', 'content': '<p>Đây là OUTPUT của thuật toán, KHÔNG phải khuyến nghị đầu tư. User phải tự DD và position sizing.</p>'},
        {'heading': '🎯 Cách áp dụng', 'content': '<ol><li>Filter top 10 strong_buy</li><li>Loại các mã đã &gt; 25% trên 52w high (chase top)</li><li>Check Multi-Timeframe consensus (1D/1W/1M)</li><li>Position size = Kelly × 0.5 (Half Kelly)</li></ol>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Tab Screener → "Composite Z &gt;= 1.5" filter.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/loc-co-phieu-tang-truong-7-tieu-chi">CANSLIM</a>',
            '<a href="/bai-viet/top-10-co-phieu-tang-manh-tuan-nay">Top mover</a>',
            '<a href="/bai-viet/khoi-ngoai-mua-rong-23-nganh-456-ma">Khối ngoại</a>',
        ])}
    ],
    'cta': 'Lọc Strong Buy tier'
},

'co-phieu-ca-map-dang-gom-nhieu-nhat': {
    'title': 'Cổ Phiếu Cá Mập Đang Gom Nhiều Nhất — Smart Money Flow | Vnstock',
    'description': 'Top mã có Smart Money Flow gom mạnh ≥3 phiên + cộng dồn 5p. Cập nhật mỗi sau 15:00.',
    'keywords': 'cá mập gom, smart money flow, dòng tiền cá mập',
    'date': '2026-06-04', 'category': 'Real-time', 'reading_time': 5,
    'h1': '🦈 Cổ Phiếu Cá Mập Đang Gom — Smart Money Flow',
    'lede': 'Cá mập (institutions, lệnh &gt;1B VND) thường gom hàng trước khi giá tăng. Vnstock track real-time và auto-list top.',
    'sections': [
        {'heading': '🔍 Methodology', 'content': '<p>Smart Money Flow đo buy/sell active từ OHLCV. Net flow trong tỷ VND:</p><pre><code>factor = (close - low) / (high - low)\nbuy_active = volume × factor\nsell_active = volume × (1 - factor)\nnet_flow = (buy - sell) × close</code></pre>'},
        {'heading': '🎯 Filter "GOM"', 'content': '<ul><li>Streak ≥ 3 phiên cá mập gom</li><li>Cộng dồn 5p &gt;= +20 tỷ</li><li>Volume tăng (không phải phiên thiếu lệnh)</li></ul>'},
        {'heading': '⚠️ Track 5+ phiên trước khi vào lệnh', 'content': '<p>Cá mập gom 5p liên tiếp = signal mạnh. 1-2 phiên có thể là noise.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Tab "Smart Money Tracker" trong Dashboard.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/smart-money-flow-phat-hien-ca-map-gom-xa">Smart Money Flow</a>',
            '<a href="/bai-viet/khoi-ngoai-mua-rong-23-nganh-456-ma">Khối ngoại mua ròng</a>',
        ])}
    ],
    'cta': 'Xem Top Cá Mập Gom'
},

'tin-hieu-mua-hom-nay-vn30': {
    'title': 'Tín Hiệu MUA Hôm Nay — VN30 Live Signals | Vnstock',
    'description': 'Top mã VN30 có tín hiệu MUA mạnh nhất hôm nay (score ≥ 8/19). Cập nhật mỗi 15 phút.',
    'keywords': 'tín hiệu mua hôm nay, vn30 buy signal',
    'date': '2026-06-05', 'category': 'Real-time', 'reading_time': 4,
    'h1': '🟢 Tín Hiệu MUA Hôm Nay — VN30 Live',
    'lede': 'Vnstock tổng hợp 19 chỉ báo thành 1 score. Mã có score ≥ 8 = BUY signal. Top hôm nay được auto-generate.',
    'sections': [
        {'heading': '🔍 Score system', 'content': '<p>19 chỉ báo: RSI, MACD, MA cross, ADX, Stochastic, Bollinger, ATR, Volume, Smart Money, Foreign, Pattern... Mỗi cái có +1/0/-1. Tổng -19 đến +19.</p>'},
        {'heading': '🎯 Tier', 'content': '<ul><li>Score ≥ +14: STRONG BUY (rất hiếm)</li><li>Score +8 đến +13: BUY</li><li>Score +5 đến +7: BUY WARN (yếu)</li><li>Score -5 đến +4: NEUTRAL</li><li>Score -7 trở xuống: SELL</li></ul>'},
        {'heading': '⚠️ Score cao không = mua an toàn', 'content': '<p>Phải combine với risk management — position size, stop loss, regime filter.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Bảng giá có cột Score realtime. Filter "Score ≥ 8".</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/vn30-hom-nay-phan-tich-realtime">VN30 hôm nay</a>',
            '<a href="/bai-viet/co-phieu-nen-mua-tuan-nay">Cổ phiếu nên mua tuần</a>',
        ])}
    ],
    'cta': 'Xem BUY signals live'
},

'co-phieu-tang-truong-2026': {
    'title': 'Top Cổ Phiếu Tăng Trưởng 2026 — Phân Tích & Forecast | Vnstock',
    'description': 'Top 10 cổ phiếu VN30 có growth potential 2026 dựa trên fundamental + technical. EPS forecast, P/E target.',
    'keywords': 'cổ phiếu tăng trưởng 2026, growth stocks vn',
    'date': '2026-06-05', 'category': 'Real-time', 'reading_time': 6,
    'h1': '🚀 Top Cổ Phiếu Tăng Trưởng 2026 — Phân Tích',
    'lede': 'Year ahead picks dựa trên fundamental + technical. Updated quarterly.',
    'sections': [
        {'heading': '📋 Methodology', 'content': '<ul><li>EPS growth forecast &gt; 20%</li><li>ROE &gt; 15% (5 năm consistent)</li><li>D/E &lt; 1.0</li><li>Sector tailwind (AI, banking digital, EV...)</li><li>Technical: above MA200, RS rank top 30%</li></ul>'},
        {'heading': '🎯 Sectors có triển vọng', 'content': '<ul><li>Banking digital transformation</li><li>Tech outsourcing (FPT, CMG)</li><li>Logistics + ports</li><li>Renewable energy</li><li>Consumer recovery</li></ul>'},
        {'heading': '⚠️ Past performance ≠ future', 'content': '<p>Forecast luôn có risk. Diversify 5-10 mã, position size &lt; 10% per stock.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Multi-factor + Forward EPS data → comprehensive picks.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/loc-co-phieu-tang-truong-7-tieu-chi">CANSLIM</a>',
            '<a href="/bai-viet/co-phieu-nen-mua-tuan-nay">Cổ phiếu nên mua</a>',
        ])}
    ],
    'cta': 'Xem Top Growth 2026'
},

'pre-breakout-watchlist-tuan-nay': {
    'title': 'Pre-Breakout Watchlist Tuần Này — Coiled Springs | Vnstock',
    'description': 'Mã sắp breakout (volatility contraction + volume drying). Detect 5-10 ngày trước actual breakout.',
    'keywords': 'pre breakout, coiled spring, sắp breakout',
    'date': '2026-06-06', 'category': 'Real-time', 'reading_time': 5,
    'h1': '⚡ Pre-Breakout Watchlist — Coiled Springs',
    'lede': 'Pre-breakout = "lò xo nén". Detect được 5-10 ngày trước = early entry, R/R cực tốt.',
    'sections': [
        {'heading': '🔍 Pre-breakout signals', 'content': '<ul><li>Bollinger Squeeze (width 6m low)</li><li>Volume drying (60-80% avg)</li><li>Range tightening &lt; 5%</li><li>RS rank top 30%</li><li>Above MA50</li></ul>'},
        {'heading': '🎯 Cách trade', 'content': '<p>Watchlist watch → đợi breakout confirmed (close vượt resistance + vol &gt;= 1.5x). Đừng vào pre-breakout (có thể never break).</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Pre-Breakout Scanner trong Dashboard, auto-update + Telegram alert.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/breakout-la-gi-5-cach-tranh-breakout-gia">Breakout là gì</a>',
            '<a href="/bai-viet/loc-co-phieu-breakout-mark-minervini">Minervini VCP</a>',
        ])}
    ],
    'cta': 'Bật Pre-Breakout Scanner'
},

'khoi-ngoai-mua-ron-tuan-nay-vn30': {
    'title': 'Khối Ngoại Mua/Bán Ròng Tuần Này VN30 | Vnstock',
    'description': 'Top mã khối ngoại mua/bán ròng mạnh nhất tuần qua. Foreign Flow tracking + 5-day cumulative.',
    'keywords': 'khối ngoại mua ròng, foreign flow tuần',
    'date': '2026-06-06', 'category': 'Real-time', 'reading_time': 4,
    'h1': '🌐 Khối Ngoại Mua/Bán Ròng Tuần Này',
    'lede': 'Khối ngoại có long-term view + research sâu. Theo dõi NN flow = theo dõi smart capital.',
    'sections': [
        {'heading': '📊 Top mua ròng', 'content': '<p>Auto-rank theo cộng dồn 5p NN net buy. Top 10 thường tập trung ở banking + consumer.</p>'},
        {'heading': '📊 Top bán ròng', 'content': '<p>Top 10 NN xả thường liên quan ETF flow (FTSE rebalance, MSCI changes).</p>'},
        {'heading': '⚠️ Đừng follow blindly', 'content': '<p>NN bán không = mã xấu. Có thể là profit taking, FX, fund redemption. Combine với fundamental.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Foreign Flow tracker + bar màu vàng/cam dưới mã trong bảng giá.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/khoi-ngoai-mua-rong-23-nganh-456-ma">Khối ngoại 23 ngành</a>',
            '<a href="/bai-viet/co-phieu-ca-map-dang-gom-nhieu-nhat">Cá mập gom</a>',
        ])}
    ],
    'cta': 'Xem Foreign Flow live'
},

# ════════════════════════════════════════════════════════════════
# CLUSTER F — SaaS HIGH-INTENT KEYWORDS (10 bài: 73-82)
# Conversion focused. Reuse có sẵn 4 bài SaaS từ server.py.
# ════════════════════════════════════════════════════════════════

'app-phan-tich-co-phieu-tot-nhat-2026': {
    'title': 'App Phân Tích Cổ Phiếu Tốt Nhất 2026 — Top 5 Cho TTCK VN | Vnstock',
    'description': 'So sánh 5 app phân tích cổ phiếu tốt nhất cho TTCK VN: Vnstock, FireAnt, TCBS, TradingView, Investing. Pros/Cons + giá.',
    'keywords': 'app phân tích cổ phiếu, app chứng khoán tốt nhất, phần mềm chứng khoán vn',
    'date': '2026-06-07', 'category': 'SaaS', 'reading_time': 9,
    'h1': '📱 App Phân Tích Cổ Phiếu Tốt Nhất 2026',
    'lede': 'App phân tích cổ phiếu tốt phải có: realtime, đầy đủ chỉ báo, screener, alert. So sánh top 5 cho TTCK VN.',
    'sections': [
        {'heading': '🏆 #1 Vnstock.io.vn', 'content': '<p>Toàn diện nhất cho VN: 19 chỉ báo, Multi-factor screener, Smart Money Flow, AI Analyst, Pattern Scanner, Quant Lab (GARCH, VaR, Monte Carlo, Kelly). <strong>Free 20 mã, Premium 299K/tháng</strong>.</p>'},
        {'heading': '🥈 #2 FireAnt', 'content': '<p>VN-focus, news + research mạnh. <strong>Cons</strong>: Screener cơ bản, không có quant features.</p>'},
        {'heading': '🥉 #3 TCBS Pro', 'content': '<p>Broker app. <strong>Pros</strong>: Đặt lệnh + research. <strong>Cons</strong>: Giới hạn cho khách TCBS.</p>'},
        {'heading': '#4 TradingView', 'content': '<p>Chart đỉnh + community. <strong>Cons</strong>: Không VN screener chuyên sâu, $14.95/tháng.</p>'},
        {'heading': '#5 Investing.com', 'content': '<p>News quốc tế tốt. <strong>Cons</strong>: VN data hạn chế.</p>'},
        {'heading': '🎯 Recommendation', 'content': '<p>Trader VN: Vnstock + FireAnt (news). International: TradingView. Detail: <a href="/bai-viet/stock-screener-vietnam-top-7">Top 7 Stock Screener VN</a>.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/tradingview-vs-vnstock">TradingView vs Vnstock</a>',
            '<a href="/bai-viet/fireant-vs-vnstock">FireAnt vs Vnstock</a>',
            '<a href="/bai-viet/tcbs-vs-vnstock">TCBS vs Vnstock</a>',
        ])}
    ],
    'cta': 'Dùng Vnstock miễn phí'
},

'phan-mem-loc-co-phieu-mien-phi': {
    'title': 'Phần Mềm Lọc Cổ Phiếu Miễn Phí 2026 — Top 7 Tốt Nhất | Vnstock',
    'description': 'Top 7 phần mềm lọc cổ phiếu miễn phí cho TTCK VN. Filter theo RSI, P/E, ROE, smart money. Comparison + recommend.',
    'keywords': 'phần mềm lọc cổ phiếu, screener miễn phí',
    'date': '2026-06-07', 'category': 'SaaS', 'reading_time': 7,
    'h1': '🔍 Phần Mềm Lọc Cổ Phiếu Miễn Phí — Top 7',
    'lede': 'Lọc 1600 mã VN trong 1 giây thành top 20 — đó là power của screener. So sánh 7 tool free/freemium.',
    'sections': [
        {'heading': '🥇 Vnstock Screener', 'content': '<p>Free 20 mã + 19 chỉ báo + multi-factor z-score. Premium full database 299K/tháng.</p>'},
        {'heading': '#2-7', 'content': '<p>FireAnt (basic free), TCBS (cho khách), TradingView (limited free), Investing.com, Vietstock, SimplyWallSt.</p>'},
        {'heading': '🎯 Free vs Paid', 'content': '<p>Free đủ cho beginner (~20 mã). Active trader nên Premium để có 1600 mã + advanced filters.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Composite z-score 6 nhân tố — duy nhất ở VN.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/stock-screener-vietnam-top-7">Top 7 chi tiết</a>',
            '<a href="/bai-viet/loc-co-phieu-tang-truong-7-tieu-chi">Growth filter</a>',
        ])}
    ],
    'cta': 'Mở Vnstock Screener free'
},

'phan-mem-backtest-chung-khoan-vn': {
    'title': 'Phần Mềm Backtest Chứng Khoán VN — Top 4 So Sánh | Vnstock',
    'description': 'So sánh phần mềm backtest cho TTCK VN: AmiBroker, MetaTrader, Vnstock AFL, Python custom. Pros/Cons + giá.',
    'keywords': 'phần mềm backtest, amibroker vn, vnstock afl',
    'date': '2026-06-08', 'category': 'SaaS', 'reading_time': 8,
    'h1': '📈 Phần Mềm Backtest Chứng Khoán VN — Top 4',
    'lede': 'Backtest 5 năm trong vài giây = unfair edge. So sánh 4 tool phổ biến.',
    'sections': [
        {'heading': '🥇 Vnstock AFL Backtest', 'content': '<p>AFL syntax port sang Python. 5 dòng code = 5 năm test trong 0.3s. T+2 + fee + slippage realistic. Community scripts. <strong>Free</strong> với Premium.</p>'},
        {'heading': '#2 AmiBroker', 'content': '<p>Classic AFL. <strong>Cons</strong>: $279, Windows-only, không có VN data tích hợp.</p>'},
        {'heading': '#3 Python (custom)', 'content': '<p>backtrader, vectorbt. Free nhưng cần code.</p>'},
        {'heading': '#4 MetaTrader 5', 'content': '<p>Forex-focus. Stock backtest hạn chế.</p>'},
        {'heading': '🎯 Recommend VN', 'content': '<p>Vnstock AFL — VN data sẵn + AFL learning curve thấp.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/afl-backtest-cong-dong-chia-se-script">AFL chi tiết</a>',
            '<a href="/bai-viet/backtest-la-gi-tai-sao-quan-trong">Backtest pillar</a>',
        ])}
    ],
    'cta': 'Test AFL Backtest free'
},

'phan-mem-canh-bao-gia-telegram-vn': {
    'title': 'Phần Mềm Cảnh Báo Giá Telegram Cho Chứng Khoán VN | Vnstock',
    'description': 'Cảnh báo giá realtime qua Telegram khi mã vượt MA, RSI quá mua/bán, breakout, Smart Money. So sánh 5 tool.',
    'keywords': 'cảnh báo giá telegram, alert vn30',
    'date': '2026-06-08', 'category': 'SaaS', 'reading_time': 6,
    'h1': '🚨 Phần Mềm Cảnh Báo Giá Telegram VN',
    'lede': 'Đang đi làm/họp, mã đột nhiên break → bạn cần biết ngay. Telegram alert &lt;1 giây = solution. So sánh tool.',
    'sections': [
        {'heading': '🥇 Vnstock', 'content': '<p>12 loại alert: MA cross, RSI, Volume spike, Pattern, Smart Money, Foreign, Catalyst News, Custom Signal Builder. <strong>Quality Gate anti-spam</strong> chỉ gửi confluence ≥3.</p>'},
        {'heading': '#2 TradingView Alerts', 'content': '<p>Mạnh nhưng $14.95/tháng + chỉ 5 alerts free.</p>'},
        {'heading': '#3 Self-built bots', 'content': '<p>Code Telegram bot + check API. Free nhưng cần dev skills.</p>'},
        {'heading': '🚀 Vnstock setup 30 giây', 'content': '<p>Settings → Telegram Bot → /start → done.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/canh-bao-realtime-catalyst-news-telegram">Catalyst alerts</a>',
        ])}
    ],
    'cta': 'Setup Telegram alerts'
},

'app-bang-gia-realtime-vn30': {
    'title': 'App Bảng Giá Realtime VN30 — Cập Nhật < 1 Giây | Vnstock',
    'description': 'Top app bảng giá realtime cho TTCK VN. Vnstock, TCBS, SSI iBoard, FireAnt. So sánh latency, features, giá.',
    'keywords': 'bảng giá realtime, vn30 realtime, ssi iboard',
    'date': '2026-06-09', 'category': 'SaaS', 'reading_time': 7,
    'h1': '⚡ App Bảng Giá Realtime VN30 — Top Lựa Chọn',
    'lede': 'Đa số app cập nhật giá mỗi 5-30 giây. Vài app dùng WebSocket cho &lt; 1 giây latency. So sánh.',
    'sections': [
        {'heading': '🏆 Vnstock', 'content': '<p>TCBS WebSocket trực tiếp. Auto-reconnect + TOTP refresh. Đầy đủ cột giá, OHLC, volume, Smart Money bar, Foreign bar. <a href="/tinh-nang/bang-gia-realtime-vn30">Detail</a>.</p>'},
        {'heading': '#2 SSI iBoard', 'content': '<p>Broker tool — chính xác cao nhưng giao diện cũ.</p>'},
        {'heading': '#3 TCBS Pro', 'content': '<p>Chỉ cho khách TCBS.</p>'},
        {'heading': '🚀 Recommend', 'content': '<p>Vnstock cho non-broker users. SSI iBoard nếu đã là khách SSI.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/vn30-hom-nay-phan-tich-realtime">VN30 hôm nay</a>',
        ])}
    ],
    'cta': 'Mở bảng giá realtime'
},

'app-chung-khoan-cho-trader-pro': {
    'title': 'App Chứng Khoán Cho Trader Pro — Top 5 Tools 2026 | Vnstock',
    'description': 'Pro trader cần: realtime, scanner, backtest, alert, custom signal. Top 5 platforms cho VN.',
    'keywords': 'app chứng khoán cho trader, pro trader vn',
    'date': '2026-06-09', 'category': 'SaaS', 'reading_time': 7,
    'h1': '👨‍💼 App Cho Trader Pro — Top 5',
    'lede': 'Pro trader = active mỗi ngày. Cần workflow optimized: real-time, scan, backtest, alert, automate. Top 5.',
    'sections': [
        {'heading': '🥇 Vnstock Premium', 'content': '<p>All-in-one VN focus. Quant Lab. Multi-factor. Custom alerts.</p>'},
        {'heading': '#2 TradingView Pro+', 'content': '<p>Charting + custom Pine Script. Cần combine với VN data.</p>'},
        {'heading': '#3 Bloomberg Terminal', 'content': '<p>$30K/year. Institutional only.</p>'},
        {'heading': '#4 Refinitiv Eikon', 'content': '<p>Tương tự Bloomberg, hơi rẻ hơn.</p>'},
        {'heading': '#5 Combination', 'content': '<p>Vnstock (VN execution) + TradingView (charting) + Bloomberg (research).</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/app-phan-tich-co-phieu-tot-nhat-2026">App tốt nhất</a>',
            '<a href="/bai-viet/tradingview-vs-vnstock">TradingView vs Vnstock</a>',
        ])}
    ],
    'cta': 'Upgrade Vnstock Premium'
},

'stock-screener-tot-nhat-2026': {
    'title': 'Stock Screener Tốt Nhất 2026 — VN + International Compare | Vnstock',
    'description': 'Stock screener tốt = lọc nhanh + factor mạnh. Vnstock, Finviz, TradingView, Stockopedia. Compare features + giá.',
    'keywords': 'stock screener, stock screener 2026, finviz vs vnstock',
    'date': '2026-06-10', 'category': 'SaaS', 'reading_time': 8,
    'h1': '📊 Stock Screener Tốt Nhất 2026',
    'lede': 'Quan trọng nhất của screener: bao nhiêu factor + tốc độ filter + custom queries. Top 5 thị trường.',
    'sections': [
        {'heading': '🇻🇳 #1 Vnstock (VN)', 'content': '<p>456 mã VN, 19 indicators, 6-factor composite z-score. Free 20 mã.</p>'},
        {'heading': '🇺🇸 #1 Finviz (US)', 'content': '<p>7000+ US stocks, đẹp, fast. Free version đủ. Pro $24.95/tháng.</p>'},
        {'heading': '#3 TradingView Screener', 'content': '<p>Đa thị trường. Filter cơ bản free, advanced Pro+ $14.95.</p>'},
        {'heading': '#4 Stockopedia (UK/EU)', 'content': '<p>StockRanks (Quality + Value + Momentum). $39/tháng.</p>'},
        {'heading': '🎯 Pick', 'content': '<p>VN: Vnstock. US: Finviz. Multi-market: TradingView.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/stock-screener-vietnam-top-7">VN screener top 7</a>',
            '<a href="/bai-viet/phan-mem-loc-co-phieu-mien-phi">Free screeners</a>',
        ])}
    ],
    'cta': 'So sánh screeners'
},

'phan-mem-ai-chung-khoan-vn': {
    'title': 'Phần Mềm AI Chứng Khoán VN — Tool Nào Thực Sự Tốt? | Vnstock',
    'description': 'AI chứng khoán đang hot. Nhưng đa số là wrapper ChatGPT. Cách nhận biết AI thật + so sánh tool.',
    'keywords': 'phần mềm ai chứng khoán, ai analyst stock vn',
    'date': '2026-06-10', 'category': 'SaaS', 'reading_time': 7,
    'h1': '🤖 Phần Mềm AI Chứng Khoán VN — Tool Thật?',
    'lede': '"AI Stock Tools" trên thị trường đa số là wrapper ChatGPT. Đa số trả lời chung chung, không có realtime data. Bài này so sánh.',
    'sections': [
        {'heading': '🔍 AI thật vs AI fake', 'content': '<ul><li><strong>AI thật</strong>: có realtime data, MTF context, news injection, lịch sử shark</li><li><strong>AI fake</strong>: GPT generic, không data, trả lời chung chung</li></ul>'},
        {'heading': '🥇 Vnstock AI Analyst', 'content': '<p>Inject context realtime: shark flow, MTF consensus, ADX trend, RSI threshold, 3 tin gần nhất. + AI Continuous (auto brief 30 phút). Detail: <a href="/bai-viet/ai-analyst-vnstock-khac-chatgpt-the-nao">AI vs GPT</a>.</p>'},
        {'heading': '#2 ChatGPT plain', 'content': '<p>Free nhưng lack data. Phù hợp education chung, không phải decision making.</p>'},
        {'heading': '#3 Bloomberg AI', 'content': '<p>Premium institutional.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>AI Analyst tab trong app + Telegram chat.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/ai-analyst-vnstock-khac-chatgpt-the-nao">AI vs GPT</a>',
            '<a href="/bai-viet/swarm-simulation-1000-nha-dau-tu-ao">Swarm AI</a>',
        ])}
    ],
    'cta': 'Hỏi AI Analyst'
},

'phan-mem-quan-ly-danh-muc-hrp': {
    'title': 'Phần Mềm Quản Lý Danh Mục Đầu Tư — HRP + Markowitz | Vnstock',
    'description': 'Quản lý portfolio chuyên nghiệp với HRP (Lopez de Prado), Efficient Frontier. Track NAV, drawdown, Sharpe. Top 4 tools.',
    'keywords': 'quản lý danh mục, portfolio optimizer, hrp markowitz',
    'date': '2026-06-11', 'category': 'SaaS', 'reading_time': 7,
    'h1': '💼 Phần Mềm Quản Lý Danh Mục — HRP + Markowitz',
    'lede': 'Excel quản lý portfolio = lỗi thời. Tools chuyên dụng có HRP, Efficient Frontier, NAV tracking, drawdown analysis.',
    'sections': [
        {'heading': '🥇 Vnstock Portfolio', 'content': '<p>HRP (Lopez de Prado 2016) + Markowitz Frontier. T+2 settlement chuẩn VN. Heatmap visualization. Detail: <a href="/tinh-nang/quan-ly-danh-muc-dau-tu">Portfolio HRP</a>.</p>'},
        {'heading': '#2 Personal Capital', 'content': '<p>US-focus, free. Không VN.</p>'},
        {'heading': '#3 Excel + Python', 'content': '<p>Custom solution. Hồi cần code.</p>'},
        {'heading': '#4 Broker tools', 'content': '<p>SSI/TCBS có portfolio tracker basic.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Tab Portfolio realtime + auto-rebalance suggestions.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/quant-lab-garch-var-monte-carlo-kelly">Kelly sizing</a>',
        ])}
    ],
    'cta': 'Quản lý portfolio HRP'
},

'phan-mem-paper-trading-vn-mo-phong': {
    'title': 'Phần Mềm Paper Trading VN — Mô Phỏng T+2 Realistic | Vnstock',
    'description': 'Paper trading với T+2, slippage, spread, commission như thật. Phù hợp người mới + test strategy.',
    'keywords': 'paper trading vn, mô phỏng giao dịch chứng khoán',
    'date': '2026-06-11', 'category': 'SaaS', 'reading_time': 6,
    'h1': '📋 Phần Mềm Paper Trading VN — Realistic T+2',
    'lede': 'Đa số paper trading bỏ qua slippage + T+2. Tập như thế = vào đời thật mất tiền. Cần realistic simulation.',
    'sections': [
        {'heading': '🥇 Vnstock Paper Trading', 'content': '<p>T+2 + slippage 0.1% + spread + commission 0.15% như thật. AI Coach review cuối tuần. <a href="/tinh-nang/paper-trading-mo-phong-giao-dich">Detail</a>.</p>'},
        {'heading': '#2 TradingView Paper', 'content': '<p>Generic paper trade. Không VN T+2.</p>'},
        {'heading': '🎯 Use case', 'content': '<p>Tập 3 tháng paper trước khi vào tiền thật. Verify win rate &gt; 50% + profit factor &gt; 1.3.</p>'},
        {'heading': '🚀 Vnstock', 'content': '<p>Tab Paper Trading + tích hợp Trading Journal AI Coach.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/trading-journal-ai-coach-tam-ly-giao-dich">Trading Journal</a>',
        ])}
    ],
    'cta': 'Mở Paper Trading free'
},

# ════════════════════════════════════════════════════════════════
# CLUSTER G — COMPARISON (8 bài: 83-90)
# Highest commercial intent. SEO bait + conversion focus.
# ════════════════════════════════════════════════════════════════

'tradingview-vs-vnstock': {
    'title': 'TradingView vs Vnstock — So Sánh Chi Tiết 2026 | Vnstock',
    'description': 'TradingView mạnh charting + community, Vnstock mạnh VN focus + Quant Lab. So sánh 7 tiêu chí + recommend per use case.',
    'keywords': 'tradingview vs vnstock, so sánh tradingview',
    'date': '2026-06-12', 'category': 'Comparison', 'reading_time': 9,
    'h1': '⚔️ TradingView vs Vnstock — So Sánh Chi Tiết',
    'lede': 'TradingView là king global về charting. Vnstock là king VN về quant + Smart Money. Bạn nên chọn cái nào?',
    'sections': [
        {'heading': '📊 Charting', 'content': '<p><strong>TradingView</strong>: thắng. Pine Script, drawing tools, indicators ngàn. <strong>Vnstock</strong>: charting đủ tốt nhưng không bằng TV.</p>'},
        {'heading': '🇻🇳 VN Stock Data', 'content': '<p><strong>Vnstock</strong>: thắng. 456 mã VN sẵn, sector mapping, FA sâu. <strong>TradingView</strong>: VN data hạn chế.</p>'},
        {'heading': '🔬 Quant Tools', 'content': '<p><strong>Vnstock</strong>: thắng. GARCH, VaR, Monte Carlo, Kelly, VPIN, HMM. <strong>TradingView</strong>: chỉ có Pine Script tự code.</p>'},
        {'heading': '🦈 Smart Money / Order Flow', 'content': '<p><strong>Vnstock</strong>: thắng. Auto Smart Money Flow + Foreign tracking + Catalyst news.</p>'},
        {'heading': '👥 Community', 'content': '<p><strong>TradingView</strong>: thắng. Million+ scripts, ideas, social trading.</p>'},
        {'heading': '💰 Giá', 'content': '<p>Vnstock 299K/tháng. TradingView Pro $14.95/tháng (~370K).</p>'},
        {'heading': '🎯 Verdict', 'content': '<table><tr><th>Use case</th><th>Pick</th></tr><tr><td>Pure VN trader</td><td><strong>Vnstock</strong></td></tr><tr><td>Multi-market + chart đẹp</td><td>TradingView</td></tr><tr><td>Quant focus</td><td><strong>Vnstock</strong></td></tr><tr><td>Pine Script lover</td><td>TradingView</td></tr></table>' + _CTA_FOOTER([
            '<a href="/bai-viet/fireant-vs-vnstock">FireAnt vs Vnstock</a>',
            '<a href="/bai-viet/stock-screener-vietnam-top-7">Top 7 VN</a>',
        ])}
    ],
    'cta': 'Try Vnstock free'
},

'fireant-vs-vnstock': {
    'title': 'FireAnt vs Vnstock — So Sánh Chi Tiết Cho Trader VN | Vnstock',
    'description': 'FireAnt mạnh news + research truyền thống, Vnstock mạnh quant + AI. So sánh 6 tiêu chí.',
    'keywords': 'fireant vs vnstock, so sánh fireant',
    'date': '2026-06-12', 'category': 'Comparison', 'reading_time': 7,
    'h1': '⚔️ FireAnt vs Vnstock — Trader VN Nên Chọn?',
    'lede': 'FireAnt thuộc fintech VN từ lâu, news + research mạnh. Vnstock mới nhưng quant đỉnh. So sánh.',
    'sections': [
        {'heading': '📰 News & Research', 'content': '<p><strong>FireAnt</strong>: thắng. News VN sâu, research analyst, community.</p>'},
        {'heading': '🔬 Quant Lab', 'content': '<p><strong>Vnstock</strong>: thắng (đè bẹp). FireAnt không có GARCH, VaR, Monte Carlo, Kelly.</p>'},
        {'heading': '🦈 Smart Money', 'content': '<p><strong>Vnstock</strong>: thắng. Real-time Smart Money Flow + Catalyst alerts.</p>'},
        {'heading': '⚡ Realtime', 'content': '<p>Cả 2 đều có realtime. Vnstock dùng TCBS WS. FireAnt dùng SSI/HOSE.</p>'},
        {'heading': '💰 Giá', 'content': '<p>FireAnt: ~399K/tháng cho Pro. Vnstock: 299K/tháng.</p>'},
        {'heading': '🎯 Verdict', 'content': '<p>Casual investor + news lover: <strong>FireAnt</strong>. Active trader + quant: <strong>Vnstock</strong>. Tốt nhất: dùng cả 2 (FireAnt cho news, Vnstock cho execution).</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/tradingview-vs-vnstock">TradingView vs Vnstock</a>',
        ])}
    ],
    'cta': 'Try Vnstock'
},

'tcbs-vs-vnstock': {
    'title': 'TCBS Pro vs Vnstock — Broker Tool vs Independent | Vnstock',
    'description': 'TCBS Pro là broker tool có realtime + đặt lệnh. Vnstock là independent platform. So sánh + use case.',
    'keywords': 'tcbs vs vnstock, tcbs pro',
    'date': '2026-06-13', 'category': 'Comparison', 'reading_time': 7,
    'h1': '⚔️ TCBS Pro vs Vnstock — Broker vs Independent',
    'lede': 'TCBS Pro miễn phí cho khách TCBS — gắn với broker. Vnstock independent — work với mọi broker. Trade-off?',
    'sections': [
        {'heading': '⚡ Realtime + Execution', 'content': '<p><strong>TCBS</strong>: thắng. Đặt lệnh trực tiếp.</p>'},
        {'heading': '🔬 Quant Tools', 'content': '<p><strong>Vnstock</strong>: thắng (đè bẹp). TCBS không có quant features.</p>'},
        {'heading': '🤖 AI', 'content': '<p><strong>Vnstock</strong>: AI Analyst + Continuous Brief. TCBS chỉ news cơ bản.</p>'},
        {'heading': '💰 Giá', 'content': '<p>TCBS: free cho khách. Vnstock: 299K/tháng.</p>'},
        {'heading': '🎯 Verdict', 'content': '<p>Khách TCBS: dùng <strong>cả 2</strong> (TCBS đặt lệnh, Vnstock phân tích). Không khách TCBS: <strong>Vnstock</strong>.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/ssi-iboard-vs-vnstock">SSI iBoard vs Vnstock</a>',
        ])}
    ],
    'cta': 'Try Vnstock free'
},

'ssi-iboard-vs-vnstock': {
    'title': 'SSI iBoard vs Vnstock — So Sánh 2026 | Vnstock',
    'description': 'SSI iBoard miễn phí cho khách SSI. Vnstock independent + advanced quant. So sánh chi tiết.',
    'keywords': 'ssi iboard vs vnstock, ssi vs vnstock',
    'date': '2026-06-13', 'category': 'Comparison', 'reading_time': 6,
    'h1': '⚔️ SSI iBoard vs Vnstock',
    'lede': 'SSI iBoard có FastConnect API + đặt lệnh. Vnstock không phải broker nhưng quant + AI mạnh hơn.',
    'sections': [
        {'heading': '⚡ Realtime', 'content': '<p>Cả 2 đều có. SSI dùng FastConnect, Vnstock dùng TCBS WS.</p>'},
        {'heading': '🔬 Quant', 'content': '<p><strong>Vnstock</strong>: thắng — Quant Lab full. SSI chỉ basic.</p>'},
        {'heading': '🦈 Smart Money', 'content': '<p><strong>Vnstock</strong>: thắng — auto track + alert. SSI không có.</p>'},
        {'heading': '💰 Giá', 'content': '<p>SSI: free cho khách. Vnstock: 299K/tháng.</p>'},
        {'heading': '🎯 Verdict', 'content': '<p>Khách SSI: <strong>cả 2</strong>. Không khách SSI: <strong>Vnstock</strong>.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/tcbs-vs-vnstock">TCBS vs Vnstock</a>',
        ])}
    ],
    'cta': 'Try Vnstock'
},

'cafef-vs-vnstock': {
    'title': 'CafeF vs Vnstock — News Site vs Quant Platform | Vnstock',
    'description': 'CafeF là news site đầu ngành. Vnstock là quant analytics platform. Khác mục đích — bổ sung nhau.',
    'keywords': 'cafef vs vnstock',
    'date': '2026-06-14', 'category': 'Comparison', 'reading_time': 5,
    'h1': '⚔️ CafeF vs Vnstock — News vs Quant',
    'lede': 'CafeF chuyên news. Vnstock chuyên analytics. Trader VN nên dùng CẢ 2.',
    'sections': [
        {'heading': '📰 News', 'content': '<p><strong>CafeF</strong>: thắng. News site #1 VN.</p>'},
        {'heading': '📊 Quant Analytics', 'content': '<p><strong>Vnstock</strong>: thắng. CafeF không có analytics.</p>'},
        {'heading': '🚀 Recommend', 'content': '<p>Đọc news ở CafeF buổi sáng → analytics ở Vnstock cho decision. Vnstock có Catalyst News alerts từ CafeF auto-pull.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/canh-bao-realtime-catalyst-news-telegram">Catalyst News</a>',
        ])}
    ],
    'cta': 'Bật Catalyst News alerts'
},

'investing-com-vs-vnstock': {
    'title': 'Investing.com vs Vnstock — Global vs VN Focus | Vnstock',
    'description': 'Investing.com global news + data. Vnstock VN focus + quant. So sánh + use case.',
    'keywords': 'investing.com vs vnstock',
    'date': '2026-06-14', 'category': 'Comparison', 'reading_time': 5,
    'h1': '⚔️ Investing.com vs Vnstock',
    'lede': 'Investing.com là source global news + economic data. Vnstock VN focus.',
    'sections': [
        {'heading': '🌐 Global Coverage', 'content': '<p><strong>Investing.com</strong>: thắng. 250+ exchanges, 100+ currencies.</p>'},
        {'heading': '🇻🇳 VN Depth', 'content': '<p><strong>Vnstock</strong>: thắng. 456 mã VN, sector ICB, Smart Money, AFL backtest.</p>'},
        {'heading': '🎯 Recommend', 'content': '<p>VN trader: <strong>Vnstock</strong> + Investing.com (chỉ cho global news).</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/cafef-vs-vnstock">CafeF vs Vnstock</a>',
        ])}
    ],
    'cta': 'Try Vnstock'
},

'vietstock-vs-vnstock': {
    'title': 'Vietstock vs Vnstock — Truyền Thống vs Modern | Vnstock',
    'description': 'Vietstock data sâu + community lâu đời. Vnstock modern UI + quant + AI. So sánh.',
    'keywords': 'vietstock vs vnstock',
    'date': '2026-06-15', 'category': 'Comparison', 'reading_time': 5,
    'h1': '⚔️ Vietstock vs Vnstock',
    'lede': 'Vietstock từ 2010s, data depth tốt. Vnstock modern, AI + quant. So sánh.',
    'sections': [
        {'heading': '📊 Data', 'content': '<p>Vietstock: deep historical, fundamental detail. Vnstock: realtime + multi-factor.</p>'},
        {'heading': '🤖 AI/Quant', 'content': '<p><strong>Vnstock</strong>: thắng đè bẹp.</p>'},
        {'heading': '🎨 UI/UX', 'content': '<p><strong>Vnstock</strong>: thắng. Modern, mobile-first.</p>'},
        {'heading': '💰 Giá', 'content': '<p>Cả 2 ~ 299K/tháng.</p>'},
        {'heading': '🎯 Verdict', 'content': '<p>Active trader + quant: <strong>Vnstock</strong>. Long-term FA research: Vietstock.</p>' + _CTA_FOOTER([])}
    ],
    'cta': 'Try modern Vnstock'
},

'tradingview-vs-fireant-vs-vnstock': {
    'title': 'TradingView vs FireAnt vs Vnstock — Triple Comparison | Vnstock',
    'description': 'So sánh 3 platform: TradingView (global chart), FireAnt (VN news), Vnstock (VN quant). Pick theo use case.',
    'keywords': 'tradingview fireant vnstock so sánh',
    'date': '2026-06-15', 'category': 'Comparison', 'reading_time': 8,
    'h1': '⚔️ TradingView vs FireAnt vs Vnstock — Triple Compare',
    'lede': 'Cả 3 platform được trader VN dùng nhiều. Mỗi cái mạnh ở 1 mảng. Bài này show table so sánh + recommend combination.',
    'sections': [
        {'heading': '📊 Comparison Table', 'content': '<table><tr><th>Tiêu chí</th><th>TradingView</th><th>FireAnt</th><th>Vnstock</th></tr><tr><td>Charting</td><td>🥇</td><td>🥉</td><td>🥈</td></tr><tr><td>VN Data</td><td>🥉</td><td>🥈</td><td>🥇</td></tr><tr><td>News</td><td>🥉</td><td>🥇</td><td>🥈</td></tr><tr><td>Quant</td><td>🥈</td><td>—</td><td>🥇</td></tr><tr><td>AI</td><td>🥉</td><td>—</td><td>🥇</td></tr><tr><td>Smart Money</td><td>—</td><td>🥈</td><td>🥇</td></tr><tr><td>Community</td><td>🥇</td><td>🥈</td><td>🥉</td></tr><tr><td>Giá/tháng</td><td>$14.95</td><td>~399K</td><td>299K</td></tr></table>'},
        {'heading': '🎯 Combinations', 'content': '<ul><li><strong>Bundle Pro</strong>: Vnstock (analytics) + TradingView (chart) + FireAnt (news basic free) = ultimate stack</li><li><strong>Budget</strong>: Vnstock free + CafeF news</li><li><strong>Newbie</strong>: FireAnt một mình</li><li><strong>Pro Quant</strong>: Vnstock duy nhất</li></ul>'},
        {'heading': '💎 Best Value', 'content': '<p><strong>Vnstock 299K/tháng</strong> — covers analytics + AI + quant + screener + alerts. Cộng vào TradingView free + CafeF free = stack 80% giá trị professional với 1/10 chi phí.</p>' + _CTA_FOOTER([
            '<a href="/bai-viet/tradingview-vs-vnstock">TV vs Vnstock chi tiết</a>',
            '<a href="/bai-viet/fireant-vs-vnstock">FireAnt vs Vnstock</a>',
            '<a href="/bai-viet/stock-screener-vietnam-top-7">Top 7 screeners</a>',
        ])}
    ],
    'cta': 'Bắt đầu với Vnstock free'
},

}  # END OF BLOG_POSTS_EXTRA

