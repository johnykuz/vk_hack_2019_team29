import React from 'react';
import PropTypes from 'prop-types';
import {Panel, PanelHeader, Link, PanelHeaderContent, List, Cell, HorizontalScroll , HeaderButton, Group, Div, platform, IOS} from '@vkontakte/vkui';
import Icon28ChevronBack from '@vkontakte/icons/dist/28/chevron_back';
import Icon24Back from '@vkontakte/icons/dist/24/back';



const osname=platform();

class Popout extends React.Component
{

render(){
	return (
	<Panel id={this.props.id}>
		<PanelHeader
			left={
				<HeaderButton onClick={this.props.go} data-to="productPage">
					{osname === IOS ? <Icon28ChevronBack/> : <Icon24Back/>}
				</HeaderButton>
			}>
			<PanelHeaderContent>
				О Товаре
			</PanelHeaderContent>
		</PanelHeader>
	</Panel>
)
}
}

export default Popout