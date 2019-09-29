import React from 'react'
import './Product.css';


function ProductCard(props){
    const imgurl = "url("+props.cover+")"
	return (
    <div className="product"  onClick={() => {props.fetchProduct(props.id)}}>
        <div className="bg"></div>
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
        <div className="productName">{(props.name.length > 20) ?  props.name.substring(0, 20)+"..." : props.name}</div>
        <div className="productCostOriginal">{props.price + " р."}</div>
        <div className="productCostNew">{(props.price*.9).toFixed()+ " р."}</div>
        <div className="productDiscount">10%</div>
    </div>)
}

export default ProductCard
