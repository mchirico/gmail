import {Injectable} from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class SearchService {
  private searchTerms: string[] = [];

  constructor() {
    console.error('0here');
  }

  putTerm(term: string) {
    this.searchTerms.push(term);
  }

  getTerms() {
    return this.searchTerms;
  }
}
