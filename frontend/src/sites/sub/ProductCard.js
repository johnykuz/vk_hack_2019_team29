import React from 'react'
import './Product.css';


function ProductCard(props){
    const imgurl = "url("+props.cover+")"
	return (
    <div className="product"  onClick={() => {props.fetchProduct(props.link)}}>
        <div className="bgd"></div>
        <div style={{
            position: 'absolute',
            width: 68,
            height: 68,
            left: 16,
            top: 4,
            background: imgurl,
            borderRadius: 5,
            backgroundSize: 'contain',
            backgroundRepeat: 'no-repeat'
        }}></div>
        <div className="productName">{props.name}</div>
        <div className="cashbackTitle">CashBack</div>
        <div className="siteDiscount">8%</div>
    </div>)
}

export default ProductCard
