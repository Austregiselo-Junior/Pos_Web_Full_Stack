import { ArrowLeft } from 'phosphor-react';
import { Nav } from 'react-bootstrap';

export function LinkBackToHome() {
  return (
    <div>
      <Nav.Link href='/'>
        <ArrowLeft size={25} weight='bold' color='red'/>
      </Nav.Link>
    </div>
  );
}
