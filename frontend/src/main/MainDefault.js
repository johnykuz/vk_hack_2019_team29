import React from 'react';
import PropTypes from 'prop-types';
import {Panel, PanelHeader, Search, List, Group, Div, Cell, platform, IOS} from '@vkontakte/vkui';
import ProductScroller from './sub/ProductScroller'
import CategoriesScroll from './sub/CategoriesScroll'

const osname=platform();

class MainDefault extends React.Component{
    render(){
        let endpoint = "https://vkmarketplace.herokuapp.com/category/"+this.props.userId+"/0"
         console.log("Main "+this.props.endpoint)
    return (
	    <Panel id={this.props.id}>
		<PanelHeader>
            Товары
		</PanelHeader>
        <Group>
            <CategoriesScroll GetCategory={(id) => this.props.GetCategory(id)}/>
        </Group>
        <Group title='Рекомендации'>
		<ProductScroller fetchProduct={(id) => this.props.fetchProduct(id)} endpoint={endpoint} />
        </Group>
    </Panel>    
    )

    }
}

export default MainDefault;
