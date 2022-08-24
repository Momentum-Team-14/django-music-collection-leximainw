for (let star of document.querySelectorAll('.favorite'))
{
    star.addEventListener('click', e => {
        console.log(star.href)
        fetch(star.href)
            .then(res => res.json())
            .then(data => {
                star.children[data.favorited + 0].classList.remove('hidden')
                star.children[1 - data.favorited].classList.add('hidden')
            })
        e.preventDefault()
    })
}