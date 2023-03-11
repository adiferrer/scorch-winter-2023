function addToCart(name, price, sale, description, image) {
  // Adds an item to the "cart"
  inDatabase = window.localStorage.getItem('cart');
  if (!inDatabase) {
    // Create the cart
    window.localStorage.setItem('cart', JSON.stringify({
      [name]: {
        price, sale, description, image, quantity: 1,
      },
    }));
  } else {
    inDatabase = JSON.parse(inDatabase);
    if (inDatabase[name]) {
      inDatabase[name].quantity += 1;
    } else {
      inDatabase[name] = {
        price, sale, description, image, quantity: 1,
      };
    }
    window.localStorage.setItem('cart', JSON.stringify(inDatabase));
  }
}

function getCart() {
  // Searches the localStorage database for items from the cart
  const cart = JSON.parse(window.localStorage.getItem('cart'));
  // for (const key in localStorage) {
  //   if (!(['length', 'clear', 'getItem', 'key', 'removeItem', 'setItem'].includes(key))) {
  //     const values = JSON.parse(window.localStorage.getItem(key));
  //     values.name = key;
  //     cart.push(values);
  //   }
  // }
  return cart;
}

function removeFromCart(name) {
  // Adds an item to the "cart"
  inDatabase = window.localStorage.getItem(name);
  if (!inDatabase) {
    // Nothing to remove
  } else {
    inDatabase = JSON.parse(inDatabase);
    if (inDatabase.quantity > 1) {
      inDatabase.quantity -= 1;
      window.localStorage.setItem(name, JSON.stringify(inDatabase));
    } else { // No more of the item in the DB
      window.localStorage.removeItem(name);
    }
  }
}
