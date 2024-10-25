import Navbar from "../utils/navBarre"
import linge from "../Assets/linge.png"

const PageProduit = (props) => {
    return (
        <>
            <Navbar />

            <div className="corps">
                <div className="gauche">
                    <img src={linge} alt="" />
                </div>
                <div className="droite">
                    <h3 className="productName"> {"Nom du produit"} </h3> 
                    <h1 className="productPrice"> {"Prix du produit"} FCFA </h1>
                    <p className="productDescription"> {"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."} </p>

                    <button>Ajouter au panier</button>

                </div>
            </div>
        </>
    )
}

export default PageProduit