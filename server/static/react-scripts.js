class WhateverYouWant extends React.Component {
    render() {
        return <div>Hello from React! The database_uri value is: {this.props.database_uri} </div>;
    }
}
ReactDOM.render(<WhateverYouWant database_uri='kala krasia'/>, document.getElementById("root"));