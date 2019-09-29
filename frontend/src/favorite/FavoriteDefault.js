import React from 'react';
import PropTypes from 'prop-types';
import {Panel, PanelHeader, List, Group, Div, Cell, platform, IOS} from '@vkontakte/vkui';
import ProductScroller from '../main/sub/ProductScroller'

const osname=platform();

const ShopcartDefault = props => (
	<Panel id={props.id}>
		<PanelHeader>
            Закладки
		</PanelHeader>
        <Group title='Мои Товары'>
		<ProductScroller fetchProduct={(id) => props.fetchProduct(id)} endpoint={"https://vkmarketplace.herokuapp.com/favourite/"+props.userId} hasMoreItemsTurnOff={true}/>
        </Group>
	</Panel>
)

ShopcartDefault.propTypes = {
	id: PropTypes.string.isRequired,
    go: PropTypes.func.isRequired,
};

export default ShopcartDefault;
