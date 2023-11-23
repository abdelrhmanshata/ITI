// ////////////////////////////////// 
// Navbar Icons
var favorite = document.getElementById("favorite");
favorite.onmouseover = function () {
    favorite.innerHTML = "favorite";
}
favorite.onmouseout = function () {
    favorite.innerHTML = "favorite_border";
}

favorite.onclick = function () {
    alert("favorite");
};

// //////////////////////////////////
// Image Slider

var image = document.getElementById("image");
var dotsContanir = document.getElementById("dots");


var index = 0;
var images = [
    "../images/slider/sliderImage1.jpg",
    "../images/slider/sliderImage2.jpg",
    "../images/slider/sliderImage3.jpg",
    "../images/slider/sliderImage4.jpg",
    "../images/slider/sliderImage5.jpg"
];

function createDots() {

    for (var i = 0; i < images.length; i++) {
        var dot = document.createElement("span");
        dot.className = "dot";
        dotsContanir.appendChild(dot);
    }
}
createDots();

var dots = document.getElementsByClassName("dot");

function selectedDot(index) {
    for (var i = 0; i < dots.length; i++) {
        if (i == index) {
            dots[i].style.backgroundColor = "#db4444";
        } else {
            dots[i].style.backgroundColor = "#bbb";
        }
    }
}

function next() {
    index += 1;
    if (index == images.length)
        index = 0;
    image.setAttribute("src", images[index % images.length]);
    selectedDot(index);
}

function previous() {
    index -= 1;
    if (index < 0)
        index = images.length - 1
    image.setAttribute("src", images[index % images.length]);
    selectedDot(index);
}

var interval;
function autoPlay() {
    interval = setInterval(next, 3000);
}

autoPlay()
// //////////////////////////////////
// Categories
var indexSelectedCategory = 0;
var categorys = document.getElementsByClassName("category");
function selectCategory(categorySelectted) {
    for (var i = 0; i < categorys.length; i++) {
        if (i == categorySelectted) {
            categorys[i].style.backgroundColor = "#db4444";
        } else {
            categorys[i].style.backgroundColor = "#fff";
        }
    }
}


// 
// Data Products

var phoneProducts = [
    {
        id: "1",
        image: "../images/products/smartphone/phone1.png",
        title: "iPhone 15 Pro Max",
        description: "iPhone 15 Pro Max (256 GB) - Black Titanium Dual Sim",
        rating: 4,
        price: "75,555 EGP",
    },
    {
        id: "2",
        image: "../images/products/smartphone/phone2.png",
        title: "iPhone 14 Pro",
        description: "Apple iPhone 14 with FaceTime - 128GB, 4GB RAM, 4G LTE, Black, Single SIM & E-SIM",
        rating: 3,
        price: "39,990 EGP",
    },
    {
        id: "3",
        image: "../images/products/smartphone/phone3.png",
        title: "Xiaomi Redmi 10",
        description: "Xiaomi Redmi 10 Dual SIM Mobile- 6.53 Inch FHD , 64GB, 4GB RAM, 4G LTE - Carbon Gray",
        rating: 2,
        price: "7,990 EGP",
    },
    {
        id: "4",
        image: "../images/products/smartphone/phone4.png",
        title: "iPhone 13 Pro",
        description: "iPhone 13 Pro (128 GB) - Yellow, Bluetooth,  Wi-Fi, USB",
        rating: 4,
        price: "45,590 EGP",
    },
    {
        id: "5",
        image: "../images/products/smartphone/phone5.png",
        title: "iPhone 12 Pro",
        description: "iPhone 12 Pro 128GB Graphite, Bluetooth,  Wi-Fi, USB",
        rating: 4,
        price: "43,900 EGP",
    }
];

var computerProducts = [
    {
        id: "1",
        image: "../images/products/computers/computer1.png",
        title: "ASUS Zenbook 14 Flip",
        description: "Laptop - AMD Ryzen 7 5800H, 16GB RAM, 1T SSD -Win 11 Home-Jade Black",
        rating: 4,
        price: "35,660 EGP",
    },
    {
        id: "2",
        image: "../images/products/computers/computer2.png",
        title: "Lenovo IdeaPad Gaming 3",
        description: "Laptop - Ryzen 5 5600H, 16GB RAM, 1TB HDD + 256GB SSD, NVIDIA GeForce RTX 3050 Ti 4GB GDDR6 , 15.6' FHD 120Hz, Backlit KB, Windows11 - Black",
        rating: 3,
        price: "30,750 EGP",
    },
    {
        id: "3",
        image: "../images/products/computers/computer3.png",
        title: "HP Victus 16-d1011ne Gaming",
        description: "Laptop, 12th Intel Core i7-12700H, 16GB RAM DDR5, 1TB NVMe SSD, NVIDIA RTX3060 6GB GDDR6, 16,1' FHD 144Hz, Backlit Keyboard, Dos, Blue",
        rating: 5,
        price: "47,438 EGP",
    },
    {
        id: "4",
        image: "../images/products/computers/computer4.png",
        title: "Lenovo Legion 5 15ACH6",
        description: "Laptop - Ryzen 5 5600H , 8 GB RAM, 512 GB SSD, NVIDIA GeForce RTX 3050 Ti 4GB GDDR6 , 15.6' FHD 120Hz, Backlit Keyboard, Windows 11",
        rating: 3,
        price: "33,120 EGP",
    },
    {
        id: "5",
        image: "../images/products/computers/computer5.png",
        title: "ASUS ROG Strix Scar 15",
        description: "Laptop G533QS-HF017T R9-5900HX 32GB 1TB SSD RTX3080 8GB 15.6' FHD 300Hz Win11 2Y Perfect Warranty",
        rating: 5,
        price: "88,280 EGP",
    }
];

var smartwatchProducts = [
    {
        id: "1",
        image: "../images/products/smartwatch/smartwatch1.png",
        title: "Apple Watch SE",
        description: "Apple Watch SE GPS 44MM Starlight Aluminum Case with Starlight Sport Band (2nd Gen - 2022)",
        rating: 5,
        price: "14,999 EGP",
    },
    {
        id: "2",
        image: "../images/products/smartwatch/smartwatch2.png",
        title: "Samsung SM-R870NZGAMEA",
        description: "Samsung SM-R870NZGAMEA Galaxy Watch4, 44mm, Green, 1 Year Warranty",
        rating: 4,
        price: "7,012 EGP",
    },
    {
        id: "3",
        image: "../images/products/smartwatch/smartwatch3.png",
        title: "HUAWEI WATCH GT 3",
        description: "HUAWEI WATCH GT 3 SE Smartwatch, Sleek and Stylish, Science-based Workouts, Sleep Health Monitoring.",
        rating: 3,
        price: "6,459 EGP",
    },
    {
        id: "4",
        image: "../images/products/smartwatch/smartwatch4.png",
        title: "Amazfit GTR 3 Pro",
        description: "Amazfit GTR 3 Pro Smart Watch for Android iPhone with Bluetooth Call Alexa GPS WiFi, Men's Fitness Tracker 150 Sports Modes, 1.45”AMOLED Display, Brown",
        rating: 4,
        price: "7,759 EGP",
    },
    {
        id: "5",
        image: "../images/products/smartwatch/smartwatch5.png",
        title: "Ultra Smartwatch 8",
        description: "Delone Smart Watch Ultra Smartwatch 8 Series 2” HD Screen Customize Dial Large Capacity Battery IP68 Waterproof (Orange)",
        rating: 2,
        price: "1,200 EGP",
    }
];

var cameraProducts = [
    {
        id: "1",
        image: "../images/products/cameras/camera1.png",
        title: "INSTAX Mini 11 Instant",
        description: "INSTAX Mini 11 Instant Film Camera - Charcoal Gray Country of origin China Brand",
        rating: 2,
        price: "2,999. EGP",
    },
    {
        id: "2",
        image: "../images/products/cameras/camera2.png",
        title: "Fujifilm Instax mini 9",
        description: "Fujifilm Instax mini 9 Instant Film Camera, Flamingo Pink",
        rating: 3,
        price: "5,499 EGP",
    },
    {
        id: "3",
        image: "../images/products/cameras/camera3.png",
        title: "CANON EOS R10",
        description: "CANON EOS R10 + RF-S 18-150mm F3.5-6.3 IS STM",
        rating: 5,
        price: "56,269 EGP",
    },
    {
        id: "4",
        image: "../images/products/cameras/camera4.png",
        title: "GoPro HERO11",
        description: "GoPro HERO11 Black - Waterproof Action Camera with 5.3K60 Ultra HD Video, 27MP Photos, 1/1.9' Image Sensor, Live Streaming, Webcam, Stabilization",
        rating: 3,
        price: "18,216 EGP",
    },
    {
        id: "5",
        image: "../images/products/cameras/camera5.png",
        title: "Fujifilm instax mini liplay",
        description: "Fujifilm instax mini liplay hybrid digital camera - blush gold",
        rating: 1,
        price: "6,049 EGP",
    }
];

var earphoneProducts = [
    {
        id: "1",
        image: "../images/products/earphones/earphone1.png",
        title: "Xiaomi Buds 3 Active",
        description: "Xiaomi Buds 3 Active Noise Cancelling modes Dual device connectivity Supports Wireless charging 32h Long battery life with Charging Case Carbon Black, 480",
        rating: 2,
        price: "2,450 EGP",
    },
    {
        id: "2",
        image: "../images/products/earphones/earphone2.png",
        title: "New bose quietcomfort 45",
        description: "New bose quietcomfort 45 bluetooth wireless noise canceling headphones - triple black",
        rating: 4,
        price: "9,999 EGP",
    },
    {
        id: "3",
        image: "../images/products/earphones/earphone3.png",
        title: "HUAWEI WATCH GT 3 ",
        description: "HUAWEI WATCH GT 3 SE Smartwatch, Sleek and Stylish, Science-based Workouts, Sleep Health Monitoring.",
        rating: 3,
        price: "6,459 EGP",
    },
    {
        id: "4",
        image: "../images/products/earphones/earphone4.png",
        title: "Amazfit GTR 3 Pro",
        description: "Amazfit GTR 3 Pro Smart Watch for Android iPhone with Bluetooth Call Alexa GPS WiFi, Men's Fitness Tracker 150 Sports Modes, 1.45”AMOLED Display, Brown",
        rating: 5,
        price: "7,759 EGP",
    },
    {
        id: "5",
        image: "../images/products/earphones/earphone5.png",
        title: "Ultra Smartwatch 8",
        description: "Delone Smart Watch Ultra Smartwatch 8 Series 2” HD Screen Customize Dial Large Capacity Battery IP68 Waterproof (Orange)",
        rating: 2,
        price: "1,200 EGP",
    }
];

//

function createRatingBar(ratingProdact) {
    var rating = document.createElement("div");
    rating.className = "rating";
    for (var i = 0; i < 5; i++) {
        var star = document.createElement("span");
        if (i < ratingProdact) {
            star.className = "fa fa-star checked";
        } else {
            star.className = "fa fa-star";
        }
        rating.appendChild(star);
    }
    return rating;
}


var Products = document.getElementById("Products");
function addProducts(dataProducts) {
    Products.innerHTML = '';
    for (var i = 0; i < 15; i++) {
        var index = i % (dataProducts.length);
        var prodectDiv = document.createElement("div");
        prodectDiv.className = "productContainer";

        var prodectimage = document.createElement("img");
        prodectimage.src = dataProducts[index].image;

        var prodecttitle = document.createElement("span");
        prodecttitle.innerHTML = dataProducts[index].title;

        var prodectdesc = document.createElement("p");
        prodectdesc.innerHTML = dataProducts[index].description;

        var ratingProdact = document.createElement("div");
        ratingProdact.className = "ratingProdact";

        // create ratingbar Prodact
        ratingProdact.append(createRatingBar(dataProducts[index].rating));

        var prodectPrice = document.createElement("span");
        prodectPrice.innerHTML = dataProducts[index].price;
        ratingProdact.append(prodectPrice);

        var prodertBtn = document.createElement("button");
        prodertBtn.className = "addCartButton";
        prodertBtn.id = `${index}`;
        prodertBtn.innerHTML = "Add Cart";

        prodectDiv.append(prodectimage, prodecttitle, prodectdesc, ratingProdact, prodertBtn);
        Products.appendChild(prodectDiv);
    }

    var addCartButtons = document.getElementsByClassName("addCartButton");

    function onClickBtnCart(event) {
        var product = dataProducts[Number(event.target.id)];
        console.log("onClick : " + product.title);
    }

    for (var i = 0; i < addCartButtons.length; i++) {
        addCartButtons[i].onclick = function (event) {
            onClickBtnCart(event);
        }
    }

}

// Select Firts Category By Default
selectCategory(0);
addProducts(phoneProducts);

categorys[0].onclick = function (event) {
    indexSelectedCategory = 0;
    selectCategory(indexSelectedCategory);
    addProducts(phoneProducts);
}

categorys[1].onclick = function (event) {
    indexSelectedCategory = 1;
    selectCategory(indexSelectedCategory);
    addProducts(computerProducts);
}

categorys[2].onclick = function (event) {
    indexSelectedCategory = 2;
    selectCategory(indexSelectedCategory);
    addProducts(smartwatchProducts);
}

categorys[3].onclick = function (event) {
    indexSelectedCategory = 3;
    selectCategory(indexSelectedCategory);
    addProducts(cameraProducts);
}

categorys[4].onclick = function (event) {
    indexSelectedCategory = 4;
    selectCategory(indexSelectedCategory);
    addProducts(earphoneProducts);
}








