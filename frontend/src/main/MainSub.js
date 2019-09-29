import React from 'react';
import PropTypes from 'prop-types';
import {Panel, HeaderButton, PanelHeader, Search, List, Group, Div, Cell, platform, IOS} from '@vkontakte/vkui';
import ProductScroller from './sub/ProductScroller'
import CategoriesScroll from './sub/CategoriesScroll'
import Icon28ChevronBack from '@vkontakte/icons/dist/28/chevron_back';
import Icon24Back from '@vkontakte/icons/dist/24/back';

const osname=platform();

class MainSub extends React.Component{
    constructor(props){
        super(props)
        this.state = {
            
        }
    }


    render(){
    return (
	    <Panel id={this.props.id}>
		<PanelHeader
			left={
				<HeaderButton onClick={this.props.go} data-to="default">
					{osname === IOS ? <Icon28ChevronBack/> : <Icon24Back/>}
				</HeaderButton>
			}>
		</PanelHeader>
        <Group title='Рекомендации'>
		<ProductScroller fetchProduct={(id) => this.props.fetchProduct(id)} endpoint={this.props.endpoint} />
        </Group>
    </Panel>    
    )

    }
}

export default MainSub;
