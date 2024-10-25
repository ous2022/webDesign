import linge from '../Assets/linge.png'

const Produit = ({nom, prix}) => {
    return(
        <div className="produit">
            <img src={linge} alt="" />
            <h2>{nom}</h2>
            <strong>{prix} FCFA</strong>
        </div>
    )
}

export default Produit