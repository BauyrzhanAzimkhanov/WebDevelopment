import {Component, EventEmitter, OnInit, Output} from '@angular/core';
import { Input } from '@angular/core';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  @Input() productList;
  @Input() arrayOfDeletedIds: number[];
  @Output() categorysBannedIds = new EventEmitter();
  // @Output() arrayOfDeletedIdsChange = new EventEmitter();
  ind: number; //
  // here visible: boolean which is = false in constructor and controlls from parent's function directly without input and output
  constructor() {
    this.ind = 0;
  }

  ngOnInit(): void {
  }
  deleteId(id: number): void
  {
    // this.categorysBannedIds.emit();
    this.ind++;
    // alert(this.countOfBannedIds + ' ' + this.productList.name);
    this.arrayOfDeletedIds.push(id);
    // alert(this.array.length + ' after');  // <<<<<<<<<<<<<<<<<<<<<
  }

}
