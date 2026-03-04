const processOrderNotWorking = (orderId) => {
  if (!orderId) {
    console.log("Invalid order ID", orderId);
    return;
  }
  let orderDetails;
  setTimeout(() => {
    console.log("Fetched order details for order ID:", orderId);
    orderDetails = { orderId, status: "Processed" };
  }, 0);

  return orderDetails;
};

// As you can see this code did not behave as expected
let initOrderId = 100;
const newOrder = processOrderNotWorking(initOrderId);
console.log("Order details:", newOrder);

// --------------------------------------------------------------------
// PROMISES
// --------------------------------------------------------------------

//TODO: How many parameters should this function take?
const processOrderPromise = (orderId) => {
  // return a promise that resolves with order details after a delay
  return new Promise((resolve, reject) => {
    if (!orderId) {
      return reject(new Error("Invalid order ID"));
    }

    setTimeout(() => {
      console.log("Fetched order details for order ID:", orderId);
      resolve({ orderId, status: "Processed" });
    }, 1000);
  });
};

// proper call to processOrderPromise:
processOrderPromise(initOrderId)
  .then((order) => {
    console.log("Order details (promise):", order);
  })
  .catch((err) => {
    console.error("Error fetching order (promise):", err.message);
  });
  
const processOrderAwait = async (orderId) => {
  //Handle error [1 Mark]
  //[HINT]: Use the promise from processOrderPromise [1 Mark]
  //[NOTE]: You do not have to return any value, console log here
  try {
    const order = await processOrderPromise(orderId);
    console.log("Order details (await):", order);
  } catch (err) {
    console.error("Error fetching order (await):", err.message);
  }
};

// call the async function with a valid id
processOrderAwait(initOrderId);
// also demonstrate error handling with invalid id
processOrderAwait(null);


