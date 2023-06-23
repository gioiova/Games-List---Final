'use strict'
  const addBtn = document.querySelector('.btn-add');
  const tbody = document.querySelector('tbody')
  const game = document.querySelector('.game');
  const rating = document.querySelector('.rating');
  const info = document.querySelector('.info');
  const divAdd = document.querySelector('.add-div');
  const plusBtn = document.querySelector('.plus');
  const overlay = document.querySelector('.overlay');
  const closeBtn = document.querySelector('.close-modal');
  const  warning = document.querySelector('.warning');


  addBtn.addEventListener('click', function(e) {
    e.preventDefault();
    if (game.value === '' || rating.value === '' || info.value === '') {
      //pass
    } else {
      const html = `
      <tr>
        <td data-label="Account">${game.value}</td>
        <td data-label="Due Date">${rating.value}</td>
        <td data-label="Amount">${info.value}</td>
      </tr>
      `
      tbody.insertAdjacentHTML('afterbegin', html);

      game.value = rating.value = info.value = '';
      divAdd.classList.add('hidden');
      overlay.classList.add('hidden');
    }
  });

  document.addEventListener('keydown', function(e) {
    if(e.key === 'Enter') {
      if (game.value === '' || rating.value === '' || info.value === '') {
        //pass
      } else {
        const html = `
        <tr>
          <td data-label="Account">${game.value}</td>
          <td data-label="Due Date">${rating.value}</td>
          <td data-label="Amount">${info.value}</td>
        </tr>
        `
        tbody.insertAdjacentHTML('afterbegin', html);

        game.value = rating.value = info.value = '';
        divAdd.classList.add('hidden');
        overlay.classList.add('hidden');
      }
    }
  })

  plusBtn.addEventListener('click', function(e) {
    e.preventDefault();
    divAdd.classList.remove('hidden');
    overlay.classList.remove('hidden')
  });

  const close = function(item) {
    item.addEventListener('click', function(e) {
      e.preventDefault();
      divAdd.classList.add('hidden');
      overlay.classList.add('hidden');
    });
  };

 close(overlay);
 close(closeBtn);

document.addEventListener('keydown', function(e) {
    if (e.key === "Escape") {
      divAdd.classList.add('hidden');
      overlay.classList.add('hidden');
    }
});
