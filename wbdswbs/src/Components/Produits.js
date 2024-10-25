import linge from '../Assets/linge.png'

const Produit = ({nomProduit, prix}) => {
    return(
        <div className="produit">
            <img src={linge} alt="" />
            <h2>{nomProduit}</h2>
            <strong>{prix} FCFA</strong>
        </div>
    )
}

export default Produit