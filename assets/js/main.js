(() => {
  const filters = document.querySelector('.filters');
  if (filters) {
    const buttons = [...filters.querySelectorAll('[data-filter]')];
    const cards = [...document.querySelectorAll('.blog-grid [data-category]')];
    const apply = (value, updateURL = false) => {
      const selected = buttons.some(button => button.dataset.filter === value) ? value : 'all';
      buttons.forEach(button => {
        const active = button.dataset.filter === selected;
        button.classList.toggle('active', active);
        button.setAttribute('aria-pressed', String(active));
      });
      cards.forEach(card => { card.hidden = selected !== 'all' && card.dataset.category !== selected; });
      document.getElementById('filter-empty').hidden = cards.some(card => !card.hidden);
      if (updateURL) {
        const url = new URL(location.href);
        if (selected === 'all') url.searchParams.delete('category');
        else url.searchParams.set('category', selected);
        history.pushState({}, '', url);
      }
    };
    filters.hidden = false;
    apply(new URL(location.href).searchParams.get('category') || 'all');
    buttons.forEach(button => button.addEventListener('click', () => apply(button.dataset.filter, true)));
    addEventListener('popstate', () => apply(new URL(location.href).searchParams.get('category') || 'all'));
  }
  const article = document.getElementById('article-content');
  const toc = document.querySelector('.toc');
  if (article && toc) {
    const headings = [...article.querySelectorAll('h2')];
    if (headings.length >= 3) {
      headings.forEach((heading, index) => {
        if (!heading.id) {
          let id = `section-${index + 1}`;
          while (document.getElementById(id)) id += '-heading';
          heading.id = id;
        }
        const item = document.createElement('li');
        const link = document.createElement('a');
        link.href = `#${heading.id}`;
        link.textContent = heading.textContent;
        item.append(link);
        document.getElementById('toc-list').append(item);
      });
      toc.hidden = false;
      if (matchMedia('(max-width: 640px)').matches) toc.querySelector('details').open = false;
    }
  }
})();
