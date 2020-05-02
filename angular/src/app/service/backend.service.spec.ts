import { TestBed } from '@angular/core/testing';
import {HttpClientModule} from '@angular/common/http';
import { BackendService } from './backend.service';
import { HttpTestingController } from '@angular/common/http/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';

import {Data} from './model/data';


// Ref: https://blog.knoldus.com/unit-testing-of-angular-service-with-httpclient/
describe('BackendService', () => {
  let service: BackendService;
  let httpMock: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientModule, HttpClientTestingModule],
      providers: [BackendService]
    });
    service = TestBed.inject(BackendService);
    httpMock = TestBed.get(HttpTestingController);
  });

  afterEach(() => {
    httpMock.verify();
  });


  it('be able to retrieve posts from the API via GET', () => {
    const dummyPosts: Data[] = [{
      userId: '1',
      id: 1,
      body: 'Hello World',
      title: 'testing Angular'
    }, {
      userId: '2',
      id: 2,
      body: 'Hello World2',
      title: 'testing Angular2'
    }];
    service.getData().subscribe(posts => {
      expect(posts.length).toBe(2);
      expect(posts).toEqual(dummyPosts);
    });
    const request = httpMock.expectOne( `${service.rooturl}/trainview`);
    expect(request.request.method).toBe('GET');
    request.flush(dummyPosts);
  });
});
