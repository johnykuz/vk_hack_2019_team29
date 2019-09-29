import React, { useState, useEffect } from 'react';
import connect from '@vkontakte/vk-connect';
import {View, Epic, Tabbar, TabbarItem, platform, IOS} from '@vkontakte/vkui';
import '@vkontakte/vkui/dist/vkui.css';
import MainDefault from './main/MainDefault'
import ProfileDefault from './profile/ProfileDefault'
import FavoriteDefault from './favorite/FavoriteDefault'
import SitesDefault from './sites/SitesDefault'

import IconMain from '@vkontakte/icons/dist/28/services_outline';
import IconProfile from '@vkontakte/icons/dist/28/user';
import IconShopcart from '@vkontakte/icons/dist/28/market_outline';
import IconFavorite from '@vkontakte/icons/dist/28/favorite';

import ProductPage from './main/ProductPage';
import CategoryPage from './main/MainSub'
import Popout from './main/Popout'

class App extends React.Component {

	constructor(props) {
		super(props);

		this.state = {
			activeStory: 'main',
			activePanel: 'default',
			wasActivePanel: null,
			fetchedUser: {id:0},
			userCard: null,
			productItem: null,
			endpoint: null,
			categorySwitch: false
		};
		this.onStoryChange = this.onStoryChange.bind(this);
		this.fetchProduct = this.fetchProduct.bind(this);
		this.GetCategory = this.GetCategory.bind(this);
	}


	postIt(postData){
		fetch('https://vkmarketplace.herokuapp.com/user/data', {
  			method: 'POST',
  			mode: "no-cors",
  			headers: {
    		'Accept': 'application/json',
    		'Content-Type': 'application/json'
    		},
    		body: JSON.stringify(postData)
    	}).then((res) => res.json())
            .then((data) =>  console.log(data))
            .catch((err)=>console.log(err))
	}

	componentDidMount() {
		connect.send('VKWebAppGetUserInfo', {});
		connect.subscribe((e) => {
			switch (e.detail.type) {
				case 'VKWebAppGetUserInfoResult':
					this.setState({ fetchedUser: e.detail.data });
					this.postIt(this.state.fetchedUser)
					break;
				default:
					console.log(e.detail.type);
			}
		});
	}

	fetchProduct(id){
		fetch("https://vkmarketplace.herokuapp.com/product/"+this.state.fetchedUser.id+"/"+id)
		.then(response => response.json())
		.then(data => {
			this.setState(prevState => {
				prevState.wasActivePanel = prevState.activePanel;
				prevState.activePanel =  "productPage";
				prevState.productItem = data.product;
				return prevState;
			})
		})
	}

	GetCategory(id){

		const user = this.state.fetchedUser.id
		this.setState({endpoint : "https://vkmarketplace.herokuapp.com/category/"+user+"/"+id})
		this.setState({activePanel:  "categoryPage"})
	}


	onStoryChange (e) {
    this.setState({ activeStory: e.currentTarget.dataset.story })
    this.setState({ activePanel: "default"})
  	}

	go = (e) => {
		this.setState({ activePanel: e.currentTarget.dataset.to })
	};

	render() {
		console.log("Render "+this.state.endpoint)
		return (
			  <Epic activeStory={this.state.activeStory} tabbar={
				<Tabbar>
					  <TabbarItem
						onClick={this.onStoryChange}
						selected={this.state.activeStory === 'profile'}
						data-story="profile"
						text="Профиль"
					  ><IconProfile /></TabbarItem>
					  <TabbarItem
						onClick={this.onStoryChange}
						selected={this.state.activeStory === 'main'}
						data-story="main"
						text="Товары"
					  ><IconMain /></TabbarItem>
					<TabbarItem
						onClick={this.onStoryChange}
						selected={this.state.activeStory === 'favorite'}
						data-story="favorite"
						text="Закладки"
					  ><IconFavorite /></TabbarItem>
					<TabbarItem
						onClick={this.onStoryChange}
						selected={this.state.activeStory === 'sites'}
						data-story="sites"
						text="Сайты"
					  ><IconShopcart /></TabbarItem>
				</Tabbar>
			  }>
			<View id = "profile" activePanel={this.state.activePanel}>
				<ProfileDefault id="default" go={this.go} fetchedUser={this.state.fetchedUser}/>
			</View>
			<View id = "main" activePanel={this.state.activePanel}>
				<MainDefault id="default" go={this.go} fetchProduct={this.fetchProduct} GetCategory={this.GetCategory} userId={this.state.fetchedUser.id}/>
				<ProductPage id="productPage" go={this.go} product={this.state.productItem} userId={this.state.fetchedUser.id} wasActivePanel={this.state.wasActivePanel}/>
				<CategoryPage id="categoryPage" go={this.go} fetchProduct={this.fetchProduct} endpoint={this.state.endpoint}/>
				<Popout id="popout" go={this.go}/>
			</View>
			<View id = "favorite" activePanel={this.state.activePanel}>
				<FavoriteDefault id="default" go={this.go} userId={this.state.fetchedUser.id} fetchProduct={this.fetchProduct}/>
				<ProductPage id="productPage" go={this.go} product={this.state.productItem}  userId={this.state.fetchedUser.id} wasActivePanel={this.state.wasActivePanel}/>
				<Popout id="popout" go={this.go}/>
			</View>
			<View id = "sites" activePanel={this.state.activePanel}>
				<SitesDefault id="default" go={this.go}/> 
			</View>
		  </Epic>
			)
		}
}

export default App;

