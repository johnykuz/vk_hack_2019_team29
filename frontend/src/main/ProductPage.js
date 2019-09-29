import React from 'react';
import PropTypes from 'prop-types';
import {Panel, PanelHeader, Link, PanelHeaderContent, List, Cell, HorizontalScroll , HeaderButton, Group, Div, platform, IOS} from '@vkontakte/vkui';
import Icon28ChevronBack from '@vkontakte/icons/dist/28/chevron_back';
import Icon24Back from '@vkontakte/icons/dist/24/back';
import './ProductPage.css'



const osname=platform();

class ProductPage extends React.Component
{
constructor(){
	super()
	this.state = {is_favourite: null}
	this.favSwitch = this.favSwitch.bind(this)
}

componentDidMount(){
	this.setState({is_favourite: this.props.product.is_favourite})
}

favSwitch(isFaved){
	const url = "https://vkmarketplace.herokuapp.com/manage_favourite/"+this.props.userId+"/"+this.props.product.id+"/"+(!isFaved?"1":"0")
	this.setState({is_favourite: !isFaved})
	fetch(url)
	.then(response => response.json())
	.then(data => {
		console.log("fetched faves")
	})

}

buyReg(){

}

buyCash(){
	
}

favButton(isFaved){
	if(isFaved){
		return (
			<img src="https://i.ibb.co/kg3NW3M/like-full.png" className="like" onClick={() => {this.favSwitch(isFaved)}}></img>
		)
	}
	else{
		return (
			<img src="https://i.ibb.co/bQbcFqx/Vector-5.png" className="like" onClick={() => {this.favSwitch(isFaved)}}></img>
		)
	}
}

render(){
	return (
	<Panel id={this.props.id}>
		<PanelHeader
			left={
				<HeaderButton onClick={this.props.go} data-to={this.props.wasActivePanel}>
					{osname === IOS ? <Icon28ChevronBack/> : <Icon24Back/>}
				</HeaderButton>
			}>
			<PanelHeaderContent>
				О Товаре
			</PanelHeaderContent>
		</PanelHeader>
		<div className="productPage">
			<div className="productImageContainer">
				<div style={{
				display: 'flex',
				height: '20em',
				background: 'url("'+this.props.product.photo_url+'")',
				backgroundSize: 'contain',
				backgroundRepeat: 'no-repeat',
				backgroundPosition: 'center',
				}}>
					{this.favButton(this.state.is_favourite)}
				</div>

			</div>
			<div className="productMetaContainerTop">
				<div className="productNewPrice">{(this.props.product.price*.9).toFixed()+" р."}</div>
				<div className="productOldPrice">{this.props.product.price+" р."}</div>
				<div className="productBuyRegRectangle" onClick={() => {window.location.href = "https://example.com"}}>
					<div className="productBuyRegName">Купить</div>
				</div>
			</div>
			<div className="productMetaContainerBottom">
				<div className="productDescription">
					{this.props.product.description}
				</div>
				<div className="productMetaContainerBottomImage">
					<div className="productBuyCashRectangle" onClick={() => {window.location.href = "https://example.com"}}>
						<div className="productBuyCashName">Хочу Дешевле</div>
					</div>
				</div>
			</div>
		</div>
	</Panel>
)
}
}

export default ProductPage