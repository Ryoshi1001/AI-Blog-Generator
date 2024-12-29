const generateBlogButton = document.getElementById('generateBlogButton');
const loadingIndicator = document.getElementById('loading-circle');
const blogContent = document.getElementById('blogContent');

generateBlogButton.addEventListener('click', async () => {
  const youtubeLink = document.getElementById('youtubeLink').value;

  if (youtubeLink) {
    console.log(youtubeLink);
    loadingIndicator.style.display = 'block';
    blogContent.innerHTML = '';
    const endpointUrl = '/generate-blog';

    try {
      const response = await fetch(endpointUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ link: youtubeLink }),
      });

      const data = await response.json();
      blogContent.innerHTML = data.content;
      loadingIndicator.style.display = 'none';
    } catch (error) {
      console.error('Error when generating Blog:', error);
      alert(
        'Something went wrong generating your Blog Post. Please try again.'
      );
      loadingIndicator.style.display = 'none';
    }
  } else {
    alert('Please enter a YouTube link.');
  }
});

