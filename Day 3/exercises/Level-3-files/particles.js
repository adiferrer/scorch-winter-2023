window.onload = function () {
  if (document.querySelector('.background') !== null) {
    Particles.init({
      selector: '.background',
      maxParticles: 210,
      connectParticles: true,
    });
  }
};
