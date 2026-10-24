(() => {
  'use strict';
  const questions = window.QUIZ_DATA;
  const letters = ['A','B','C','D'];
  const storageKey = 'comp3670-quiz-selftest-v1';
  let answers = loadAnswers();
  let filter = 0;
  let currentIndex = questions.findIndex(q => !answers[q.id]);
  if (currentIndex < 0) currentIndex = 0;
  const $ = id => document.getElementById(id);

  function loadAnswers() {
    try {
      const saved = JSON.parse(localStorage.getItem(storageKey) || '{}');
      return saved && typeof saved === 'object' ? saved : {};
    } catch { return {}; }
  }
  function saveAnswers() {
    try { localStorage.setItem(storageKey, JSON.stringify(answers)); } catch {}
  }
  function visibleIndices() {
    return questions.map((q,i) => q.quiz === filter || filter === 0 ? i : -1).filter(i => i >= 0);
  }
  function selectIndex(index) {
    currentIndex = index;
    render();
    window.scrollTo({top: 0, behavior: 'smooth'});
  }
  function buildSelector() {
    const select = $('quizSelect');
    select.innerHTML = '<option value="0">全部 Quiz（42 题）</option>' +
      Array.from({length:11},(_,i) => {
        const n = i+1;
        const count = questions.filter(q => q.quiz === n).length;
        return `<option value="${n}">Quiz ${String(n).padStart(2,'0')}（${count} 题）</option>`;
      }).join('');
    select.addEventListener('change', () => {
      filter = Number(select.value);
      const indices = visibleIndices();
      if (!indices.includes(currentIndex)) currentIndex = indices.find(i => !answers[questions[i].id]) ?? indices[0];
      render();
    });
  }
  function render() {
    const q = questions[currentIndex];
    const indices = visibleIndices();
    const position = indices.indexOf(currentIndex);
    const selected = answers[q.id];
    const correct = selected === q.answer;
    const answeredCount = questions.filter(item => answers[item.id]).length;
    const correctCount = questions.filter(item => answers[item.id] === item.answer).length;
    $('answeredCount').textContent = answeredCount;
    $('correctCount').textContent = correctCount;
    $('accuracy').textContent = answeredCount ? Math.round(correctCount / answeredCount * 100) + '%' : '—';
    $('progressFill').style.width = `${answeredCount / questions.length * 100}%`;
    $('progressTrack').setAttribute('aria-valuenow', answeredCount);
    $('quizBadge').textContent = `QUIZ ${String(q.quiz).padStart(2,'0')}`;
    $('questionPosition').textContent = `第 ${q.number} 题 / 共 ${questions.filter(item => item.quiz === q.quiz).length} 题`;
    $('questionNumber').textContent = String(q.number).padStart(2,'0');
    $('questionLabel').textContent = q.label;
    $('prompt').innerHTML = q.promptHtml;
    const status = $('questionStatus');
    status.textContent = selected ? (correct ? '回答正确' : '回答错误') : '待作答';
    status.className = 'status-chip' + (selected ? (correct ? ' correct' : ' incorrect') : '');

    const options = $('options');
    options.replaceChildren();
    for (const option of q.options) {
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'option';
      if (selected && option.letter === q.answer) button.classList.add('correct');
      if (selected && option.letter === selected && selected !== q.answer) button.classList.add('incorrect');
      button.disabled = Boolean(selected);
      button.setAttribute('aria-label', `${option.letter} 选项`);
      const key = document.createElement('span');
      key.className = 'option-key';
      key.textContent = option.letter;
      const content = document.createElement('span');
      content.className = 'option-content';
      content.innerHTML = option.html;
      button.append(key, content);
      button.addEventListener('click', () => choose(option.letter));
      options.append(button);
    }
    const panel = $('answerPanel');
    panel.hidden = !selected;
    if (selected) {
      panel.className = 'answer-panel' + (correct ? '' : ' wrong');
      panel.replaceChildren();
      const title = document.createElement('div');
      title.className = 'answer-title';
      title.textContent = (correct ? '✓ 答对了' : '✕ 答错了') + ` · 正确答案 ${q.answer}`;
      const explanation = document.createElement('p');
      explanation.textContent = q.explanation;
      panel.append(title, explanation);
    }
    $('sourceLinks').innerHTML = `<a href="${q.questionPdf}" target="_blank" rel="noopener">查看原题 ↗</a><a href="${q.answerPdf}" target="_blank" rel="noopener">查看原 PDF 答案 ↗</a>`;
    $('pagerCount').textContent = `${position+1} / ${indices.length}`;
    $('prevButton').disabled = position === 0;
    $('nextButton').disabled = position === indices.length-1;
    const map = $('questionMap');
    map.replaceChildren();
    indices.forEach((index,i) => {
      const item = questions[index];
      const button = document.createElement('button');
      button.type = 'button';
      button.className = 'map-button';
      if (answers[item.id]) button.classList.add(answers[item.id] === item.answer ? 'answered' : 'wrong');
      if (index === currentIndex) button.classList.add('active');
      button.textContent = i+1;
      button.setAttribute('aria-label', `第 ${i+1} 题${answers[item.id] ? '，已答' : ''}`);
      button.addEventListener('click', () => selectIndex(index));
      map.append(button);
    });
  }
  function choose(letter) {
    const q = questions[currentIndex];
    if (answers[q.id]) return;
    answers[q.id] = letter;
    saveAnswers();
    render();
    $('answerPanel').scrollIntoView({behavior:'smooth', block:'nearest'});
  }
  function move(delta) {
    const indices = visibleIndices();
    const position = indices.indexOf(currentIndex) + delta;
    if (position >= 0 && position < indices.length) selectIndex(indices[position]);
  }
  $('prevButton').addEventListener('click', () => move(-1));
  $('nextButton').addEventListener('click', () => move(1));
  $('resetButton').addEventListener('click', () => {
    const text = filter ? `重做 Quiz ${filter} 的全部题目？` : '重做全部 42 道题目？';
    if (!window.confirm(text)) return;
    visibleIndices().forEach(index => delete answers[questions[index].id]);
    saveAnswers();
    currentIndex = visibleIndices()[0];
    render();
  });
  document.addEventListener('keydown', event => {
    if (event.target instanceof HTMLElement && ['INPUT','SELECT','TEXTAREA','BUTTON'].includes(event.target.tagName)) return;
    if (['1','2','3','4'].includes(event.key)) { choose(letters[Number(event.key)-1]); event.preventDefault(); }
    if (event.key === 'ArrowLeft') { move(-1); event.preventDefault(); }
    if (event.key === 'ArrowRight') { move(1); event.preventDefault(); }
  });
  buildSelector();
  render();
})();
