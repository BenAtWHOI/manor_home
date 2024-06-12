import { Slide } from "react-slideshow-image";
import "react-slideshow-image/dist/styles.css";
import './Slideshow.css';

const Slideshow = () => {
  const images = [
    'https://www.whoi.edu/wp-content/uploads/2019/01/ArmstrongMain_424553.jpg',
    'https://www.whoi.edu/wp-content/uploads/2019/01/atlantis_main_en1_36169.jpg',
    'https://www.whoi.edu/wp-content/uploads/2019/01/TiogaMain_424494.jpg'
  ]

  return (
    <div class='container'>
      <Slide easing="ease" pauseOnHover={false} arrows={false} canSwipe={false}>
        {images.map((image, index) => {
          return (
            <div class="slide" key={image}>
              <div style={{
                backgroundImage: `url(${images[index]})`,
                backgroundSize: 'cover',
                backgroundRepeat: 'no-repeat',
                backgroundPosition: 'center'
              }}></div>
            </div>
          );
        })}
      </Slide>
    </div>
  );
}

export default Slideshow