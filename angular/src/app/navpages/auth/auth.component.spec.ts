import {async, ComponentFixture, TestBed} from '@angular/core/testing';
import {AngularFireAuth} from '@angular/fire/auth';

import {AuthComponent} from './auth.component';

describe('AuthComponent', () => {
  let component: AuthComponent;
  let fixture: ComponentFixture<AuthComponent>;

  const valueAngularFireAuthSpy = jasmine.createSpyObj('AngularFireAuth',
    ['signInWithPopup', 'signOut']);

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [AuthComponent],
      providers: [
        {provide: AngularFireAuth, useValue: valueAngularFireAuthSpy},
      ]
    })
      .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AuthComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should logout', () => {
    component.logout()
    expect(valueAngularFireAuthSpy.signOut).toHaveBeenCalled()
  });
});

