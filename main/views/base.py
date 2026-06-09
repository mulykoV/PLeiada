from django.http import HttpResponse

def home_page(request):
    html_content = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ПЛЕЯДА — Простір українських думок та літератури</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;1,300;1,400&family=Spectral:ital,wght@0,300;1,300;1,400&display=swap" rel="stylesheet">
    <style>
        *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

        :root {
            --ink:      #1A1A1A;
            --ink-soft: #2A2421;
            --muted:    #6E655F;
            --ghost:    #8C827A;
            --paper:    #FDFBF7;
            --paper-2:  #FAF5EC;
            --ochre:    #A67C52;
            --rule:     rgba(26, 26, 26, 0.12);
        }

        body {
            font-family: 'Cormorant Garamond', serif;
            background-color: var(--paper);
            color: var(--ink);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            overflow-x: hidden;
        }

        .p-full-width { width: 100%; }

        .p-container {
            width: 100%;
            max-width: 1040px;
            margin: 0 auto;
        }

        .p-rule {
            width: 100vw;
            height: 0.5px;
            background-color: var(--rule);
            position: relative;
            left: 50%;
            transform: translateX(-50%);
        }

        /* ── НАВІГАЦІЯ РОЗТЯГНУТА ПО КРАЯХ ── */
        .p-nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 2.5rem 5rem;
            width: 100%;
        }

        .p-nav-brand {
            display: flex;
            align-items: center;
            gap: 16px;
            text-decoration: none;
        }

        .p-nav-wordmark {
            font-size: 1.5rem;
            letter-spacing: 0.45em;
            color: var(--ink);
            font-weight: 500;
        }

        .p-nav-links { display: flex; gap: 1.5rem; align-items: center; }

        .p-btn-ghost {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.15rem;
            letter-spacing: 0.14em;
            padding: 10px 20px;
            border: none;
            background: transparent;
            color: var(--muted);
            cursor: pointer;
            text-decoration: none;
            transition: color 0.3s;
        }
        .p-btn-ghost:hover { color: var(--ink); }

        .p-btn-solid {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.15rem;
            letter-spacing: 0.14em;
            padding: 12px 28px;
            border: 0.5px solid var(--ink);
            background: var(--ink);
            color: var(--paper);
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            transition: background 0.3s;
        }
        .p-btn-solid:hover { background: #3a3a3a; }

        /* ── ГЕРОЙ СЕКЦІЯ ── */
        .p-hero {
            padding: 6rem 3rem 7rem;
            text-align: center;
        }

        /* Фіксоване сузір'я */
        .p-constellation-wrap {
            width: 130px;
            margin: 0 auto 2.5rem;
            display: flex;
            justify-content: center;
            align-items: center;
            opacity: 0.85;
        }

        /* ДИНАМІЧНИЙ ШРИФТ ЛІТЕР */
        .p-dynamic-title {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 0.05em;
            margin: 0 0 1.5rem;
            user-select: none;
        }
        
        .p-dynamic-title span {
            font-size: 8rem;
            font-weight: 300;
            color: var(--ink);
            display: inline-block;
            transform-origin: center bottom;
        }

        .p-letter-1 { animation: letterDance1 8s ease-in-out infinite alternate; }
        .p-letter-2 { animation: letterDance2 7s ease-in-out infinite alternate 1s; }
        .p-letter-3 { animation: letterDance3 9s ease-in-out infinite alternate 0.5s; }
        .p-letter-4 { animation: letterDance4 6s ease-in-out infinite alternate 2s; }
        .p-letter-5 { animation: letterDance1 7.5s ease-in-out infinite alternate 1.5s; }
        .p-letter-6 { animation: letterDance2 8.5s ease-in-out infinite alternate 0.2s; }

        @keyframes letterDance1 {
            0%, 100% { font-style: normal; font-weight: 300; transform: scale(1); }
            50% { font-style: italic; font-weight: 400; transform: scale(1.02) skewX(-2deg); }
        }
        @keyframes letterDance2 {
            0%, 100% { font-style: italic; font-weight: 300; transform: rotate(0deg); }
            50% { font-style: normal; font-weight: 500; transform: scale(0.98) rotate(1deg); }
        }
        @keyframes letterDance3 {
            0%, 100% { font-weight: 400; font-style: normal; }
            50% { font-weight: 300; font-style: italic; }
        }
        @keyframes letterDance4 {
            0%, 100% { transform: scale(1); font-weight: 500; }
            50% { transform: scale(1.04); font-weight: 300; font-style: normal; }
        }

        .p-tagline {
            font-family: 'Spectral', serif;
            font-style: italic;
            font-weight: 300;
            font-size: 1.75rem;
            color: var(--muted);
            letter-spacing: 0.08em;
            margin: 0 0 5rem;
        }

        .p-ornament {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 24px;
            margin: 0 auto 5rem;
            opacity: 0.5;
        }
        .p-ornament-line { width: 140px; height: 0.5px; background: var(--ink); }

        .p-book-layout {
            max-width: 760px;
            margin: 0 auto;
            text-align: justify;
            text-justify: inter-word;
        }

        .p-manifesto-paragraph {
            font-weight: 300;
            font-size: 1.95rem;
            line-height: 2;
            color: var(--ink-soft);
            margin-bottom: 2.5rem;
            text-indent: 2.5rem;
        }

        .p-hero-blockquote {
            font-family: 'Spectral', serif;
            font-style: italic;
            font-size: 2.2rem;
            color: var(--ochre);
            text-align: center;
            margin: 5rem 0;
            line-height: 1.8;
            font-weight: 300;
        }
        .p-hero-blockquote-attr {
            font-family: 'Cormorant Garamond', serif;
            font-style: normal;
            font-size: 1.1rem;
            letter-spacing: 0.25em;
            text-transform: uppercase;
            color: var(--ghost);
            display: block;
            margin-top: 1.2rem;
        }

        /* ── ОБИТЕЛІ (ЧИСТИЙ FLEX) ── */
        .p-chapters-section {
            padding: 6rem 3rem;
            max-width: 860px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            width: 100%;
        }
        
        .p-chapter {
            margin-bottom: 5.5rem;
            display: flex;
            gap: 4rem;
            align-items: flex-start;
            text-align: left;
            width: 100%;
        }
        .p-chapter:last-child { margin-bottom: 0; }

        .p-chapter-meta {
            font-size: 1.15rem;
            letter-spacing: 0.3em;
            color: var(--ochre);
            text-transform: uppercase;
            font-weight: 500;
            padding-top: 8px;
            min-width: 160px;
        }

        .p-chapter-body { flex: 1; }

        .p-chapter-title {
            font-size: 2.4rem;
            font-weight: 400;
            letter-spacing: 0.02em;
            color: var(--ink);
            margin-bottom: 1rem;
        }

        .p-chapter-desc {
            font-family: 'Spectral', serif;
            font-style: italic;
            font-weight: 300;
            font-size: 1.35rem;
            line-height: 1.85;
            color: var(--muted);
        }

        /* ── ОРАКУЛ-КНИГА ── */
        .p-oracle-wrap {
            width: 100vw;
            position: relative;
            left: 50%;
            transform: translateX(-50%);
            background-color: var(--paper-2);
            padding: 8rem 3rem;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            border-top: 0.5px solid var(--rule);
            border-bottom: 0.5px solid var(--rule);
        }

        .p-oracle-title {
            font-size: 2rem;
            letter-spacing: 0.25em;
            margin-bottom: 1rem;
            font-weight: 400;
            text-transform: uppercase;
        }

        .p-oracle-hint {
            font-family: 'Spectral', serif;
            font-style: italic;
            font-size: 1.3rem;
            color: var(--ghost);
            margin-bottom: 4.5rem;
        }

        .p-opened-book {
            width: 100%;
            max-width: 820px;
            min-height: 300px;
            background: #FDFBF7;
            border: 1px solid rgba(26,26,26,0.08);
            box-shadow: 0 20px 50px rgba(42,36,33,0.05);
            padding: 4.5rem;
            position: relative;
            margin-bottom: 4.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .p-opened-book::before {
            content: '';
            position: absolute;
            top: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 2px;
            height: 100%;
            background: linear-gradient(90deg, rgba(0,0,0,0.03) 0%, rgba(0,0,0,0.01) 100%);
            box-shadow: 0 0 14px rgba(26,26,26,0.09);
        }

        #p-quote-display {
            font-family: 'Spectral', serif;
            font-style: italic;
            font-size: 2.2rem;
            line-height: 1.85;
            color: var(--ink-soft);
            max-width: 700px;
            margin: 0 auto;
            transition: opacity 0.35s ease-in-out, transform 0.35s ease-in-out;
            opacity: 1;
            text-align: center;
        }

        #p-quote-display .attr {
            display: block;
            font-family: 'Cormorant Garamond', serif;
            font-style: normal;
            font-weight: 500;
            font-size: 1.35rem;
            letter-spacing: 0.25em;
            text-transform: uppercase;
            color: var(--ochre);
            margin-top: 2.5rem;
        }

        .p-btn-oracle {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.15rem;
            letter-spacing: 0.25em;
            padding: 16px 48px;
            border: 0.5px solid var(--ink);
            background: transparent;
            color: var(--ink);
            cursor: pointer;
            text-transform: uppercase;
            transition: all 0.3s;
        }
        .p-btn-oracle:hover { background: var(--ink); color: var(--paper); }

        /* ── CTA ── */
        .p-cta { padding: 9rem 3rem; text-align: center; }

        .p-cta-text {
            font-family: 'Spectral', serif;
            font-style: italic;
            font-weight: 300;
            font-size: 2.2rem;
            color: var(--ink-soft);
            margin: 0 0 5rem;
            line-height: 2;
        }

        .p-cta-btns { display: flex; gap: 2rem; justify-content: center; flex-wrap: wrap; }

        .p-btn-cta {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.25rem;
            letter-spacing: 0.2em;
            padding: 22px 54px;
            border: 0.5px solid var(--ink);
            background: var(--ink);
            color: var(--paper);
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s;
            text-transform: uppercase;
        }
        .p-btn-cta:hover { background: #3a3a3a; transform: translateY(-1px); }

        .p-btn-cta-out {
            font-family: 'Cormorant Garamond', serif;
            font-size: 1.25rem;
            letter-spacing: 0.2em;
            padding: 22px 54px;
            border: 0.5px solid rgba(26,26,26,0.35);
            background: transparent;
            color: var(--ink);
            cursor: pointer;
            text-decoration: none;
            display: inline-block;
            transition: all 0.3s;
            text-transform: uppercase;
        }
        .p-btn-cta-out:hover { background: rgba(26,26,26,0.05); transform: translateY(-1px); }

        /* ── ФУТЕР ── */
        .p-footer {
            padding: 4rem 5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }

        .p-footer-city {
            font-size: 1.1rem;
            letter-spacing: 0.35em;
            color: var(--ghost);
            text-transform: uppercase;
        }

        @keyframes starTwinkle {
            0%, 100% { opacity: 0.3; transform: scale(0.9); }
            50% { opacity: 1; transform: scale(1.1); }
        }
        .s-twinkle-1 { animation: starTwinkle 3s infinite ease-in-out; }
        .s-twinkle-2 { animation: starTwinkle 4.5s infinite ease-in-out 0.5s; }
        .s-twinkle-3 { animation: starTwinkle 2.5s infinite ease-in-out 1.2s; }
    </style>
</head>
<body>

    <!-- НАВІГАЦІЯ З МОНОГРАМОЮ «П» -->
    <div class="p-full-width">
        <nav class="p-nav">
            <a href="/" class="p-nav-brand">
                <!-- Витончений преміальний мінімалізм: геометрична П з лінією розколу (корінця книги) -->
                <svg width="32" height="32" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="Логотип Плеяди">
                    <path d="M6,28 L6,6 L26,6 L26,28" stroke="#1A1A1A" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                    <line x1="16" y1="6" x2="16" y2="28" stroke="#A67C52" stroke-width="1.2" stroke-dasharray="2,2"/>
                </svg>
                <span class="p-nav-wordmark">ПЛЕЯДА</span>
            </a>
            <div class="p-nav-links">
                <a class="p-btn-ghost" href="/login/">Вхід до обителі</a>
                <a class="p-btn-solid" href="/register/">Внести ім'я до реєстру</a>
            </div>
        </nav>
    </div>

    <div class="p-rule"></div>

    <!-- ГОЛОВНИЙ МАНІФЕСТ -->
    <div class="p-container">
        <div class="p-hero">
            
            <div class="p-constellation-wrap">
                <svg width="120" height="85" viewBox="0 0 110 80" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                    <line x1="20" y1="50" x2="40" y2="35" stroke="#6E655F" stroke-width="0.6" opacity="0.3"/>
                    <line x1="40" y1="35" x2="60" y2="24" stroke="#6E655F" stroke-width="0.6" opacity="0.3"/>
                    <line x1="60" y1="24" x2="66" y2="46" stroke="#6E655F" stroke-width="0.6" opacity="0.35"/>
                    <line x1="66" y1="46" x2="82" y2="40" stroke="#6E655F" stroke-width="0.6" opacity="0.3"/>
                    <line x1="46" y1="55" x2="66" y2="46" stroke="#6E655F" stroke-width="0.6" opacity="0.35"/>
                    <line x1="46" y1="55" x2="53" y2="68" stroke="#6E655F" stroke-width="0.6" opacity="0.3"/>

                    <circle class="s-twinkle-1" cx="20" cy="50" r="3.2" fill="#6E655F"/>
                    <circle class="s-twinkle-2" cx="40" cy="35" r="2.5" fill="#6E655F"/>
                    <circle class="s-twinkle-3" cx="46" cy="55" r="4" fill="#1A1A1A"/>
                    <circle class="s-twinkle-1" cx="60" cy="24" r="2.8" fill="#6E655F"/>
                    <circle class="s-twinkle-2" cx="66" cy="46" r="4.5" fill="#1A1A1A"/>
                    <circle class="s-twinkle-3" cx="82" cy="40" r="2.5" fill="#6E655F"/>
                    <circle class="s-twinkle-1" cx="53" cy="68" r="2.2" fill="#6E655F"/>
                </svg>
            </div>
            
            <div class="p-dynamic-title" aria-label="Плеяда">
                <span class="p-letter-1">П</span>
                <span class="p-letter-2">Л</span>
                <span class="p-letter-3">Е</span>
                <span class="p-letter-4">Я</span>
                <span class="p-letter-5">Д</span>
                <span class="p-letter-6">А</span>
            </div>
            
            <p class="p-tagline">простір українських думок та літератури</p>

            <div class="p-ornament">
                <div class="p-ornament-line"></div>
                <svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">
                    <path d="M7,0 L7,14 M0,7 L14,7 M2,2 L12,12 M12,2 L2,12" stroke="#1A1A1A" stroke-width="0.8" stroke-linecap="round"/>
                </svg>
                <div class="p-ornament-line"></div>
            </div>

            <div class="p-book-layout">
                <p class="p-manifesto-paragraph">Є простори, де час уповільнює свій біг, поступаючись місцем чистому й неквапливому Слову. Де текст позбавляється галасу, алгоритмічного тиску та цифрового сміття, а щира, вистраждана думка шукає свого справжнього, глибокого читача.</p>
                
                <div class="p-hero-blockquote">
                    «Слово — то мудрості промінь живий...»
                    <span class="p-hero-blockquote-attr">— Леся Wikipedia</span>
                </div>

                <p class="p-manifesto-paragraph">Плеяда постає як затишна, шляхетна обитель для тих, хто тче нові художні та філософські сенси сучасної української культури. Це простір для тих, хто пише від самого серця, і для тих, хто вміє читати до останньої крапки.</p>
            </div>
        </div>
    </div>

    <div class="p-rule"></div>

    <!-- ОБИТЕЛІ (РІВНИЙ ФІКС) -->
    <div class="p-container">
        <div class="p-chapters-section">
            
            <div class="p-chapter">
                <div class="p-chapter-meta">Розділ перший</div>
                <div class="p-chapter-body">
                    <h2 class="p-chapter-title">Амфітеатр</h2>
                    <p class="p-chapter-desc">Сценічний простір думок. Твоя поезія розквітає ліричним модерновим штибом, а проза постає перед світом як шляхетна мініатюрна книга, готова розкрити свої таємниці при першому дотику.</p>
                </div>
            </div>

            <div class="p-chapter">
                <div class="p-chapter-meta">Розділ другий</div>
                <div class="p-chapter-body">
                    <h2 class="p-chapter-title">Робоче Бюрко</h2>
                    <p class="p-chapter-desc">Особистий творчий вівтар письменника. Сховище твоїх затишних чернеток, розчерків чорнильного пера та резонансних рукописів, що матеріалізуються на стіні спогадів.</p>
                </div>
            </div>

            <div class="p-chapter">
                <div class="p-chapter-meta">Розділ третій</div>
                <div class="p-chapter-body">
                    <h2 class="p-chapter-title">Бібліотеки</h2>
                    <p class="p-chapter-desc">Тихі інтелектуальні союзи однодумців. Можливість створювати спільні книжкові полиці, вести закриті кола палких обговорень та оберігати власні вечірні ритуали читання.</p>
                </div>
            </div>

        </div>
    </div>

    <!-- ОРАКУЛ -->
    <div class="p-oracle-wrap">
        <h3 class="p-oracle-title">Пошук резонансу</h3>
        <p class="p-oracle-hint">Торкніться сторінок розгорнутого альманаху навмання</p>

        <div class="p-opened-book">
            <div id="p-quote-display">
                «Книга відкриває вічність для тих, хто вміє слухати тишу...»
            </div>
        </div>

        <button type="button" class="p-btn-oracle" id="oracle-btn">Перегорнути сторінку</button>
    </div>

    <div class="p-rule"></div>

    <!-- CTA -->
    <div class="p-container">
        <div class="p-cta">
            <p class="p-cta-text">
                Поки мільйони людей безцільно гортають нескінченні цифрові стрічки,<br>
                ми збираємо тих, хто готовий зануритися в глибину живого слова.
            </p>
            <div class="p-cta-btns">
                <a class="p-btn-cta" href="/register/">Залишити свій розчерк пера</a>
                <a class="p-btn-cta-out" href="/login/">Вхід до обителі</a>
            </div>
        </div>
    </div>

    <div class="p-rule"></div>

    <!-- ФУТЕР -->
    <div class="p-full-width">
        <footer class="p-footer">
            <span class="p-footer-city">Київ · 2026</span>
            <svg width="22" height="22" viewBox="0 0 32 32" fill="none" xmlns="http://www.w3.org/2000/svg" style="opacity: 0.45">
                <path d="M6,28 L6,6 L26,6 L26,28" stroke="#1A1A1A" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
                <line x1="16" y1="6" x2="16" y2="28" stroke="#A67C52" stroke-width="1.2" stroke-dasharray="2,2"/>
            </svg>
            <span class="p-footer-city">ПЛЕЯДА</span>
        </footer>
    </div>

    <script>
        const quotes = [
            { text: '«Слово — то мудрості промінь живий, сповнений світла й краси...»', attr: '— Леся Українка' },
            { text: '«З усіх утрат втрата часу найтяжча. Але книга дарує нам вічність.»', attr: '— Григорій Сковорода' },
            { text: '«Лупайте сю скалу! Нехай ні жар, ні холод не спинить вас.»', attr: '— Іван Франко' },
            { text: '«Ми не маємо права не бути геніальними, коли наша земля така прекрасна.»', attr: '— Ліна Костенко' },
            { text: '«Терпи, терпи — терпець тебе шліфує, сталить твій дух...»', attr: '— Василь Стус' },
            { text: '«Щоб вирости, треба спочатку пустити глибоке коріння в мовчання.»', attr: '— Ольга Кобилянська' },
            { text: '«Писати — означає витягувати з темряви те, що прагне стати світлом.»', attr: '— Маніфест Плеяди' }
        ];

        let currentIdx = -1;
        const display = document.getElementById('p-quote-display');
        const btn = document.getElementById('oracle-btn');

        btn.addEventListener('click', function(e) {
            e.preventDefault(); 
            display.style.opacity = '0';
            setTimeout(function() {
                let idx;
                do { idx = Math.floor(Math.random() * quotes.length); }
                while (idx === currentIdx);
                currentIdx = idx;
                const q = quotes[idx];
                display.innerHTML = q.text + '<span class="attr">' + q.attr + '</span>';
                display.style.opacity = '1';
            }, 300);
        });
    </script>

</body>
</html>"""
    return HttpResponse(html_content)