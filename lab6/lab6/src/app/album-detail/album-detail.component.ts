import { Component, OnInit } from '@angular/core';
import {Album} from '../album-matrix';
import {ActivatedRoute} from '@angular/router';
import {Albums} from '../test-albums';
import {Location} from '@angular/common';
import {AlbumsService} from '../albums.service';

@Component({
  selector: 'app-album-detail',
  templateUrl: './album-detail.component.html',
  styleUrls: ['./album-detail.component.css']
})
export class AlbumDetailComponent implements OnInit{
  updateTitle: string;
  // @ts-ignore
  album: Album = {id: 5, title: 'sf1000'}; ///// have to initialize
  // @ts-ignore
  loading: boolean;
  constructor(private route: ActivatedRoute,
              private location: Location,
              private  albumsService: AlbumsService){
    this.updateTitle = '';
  }

  ngOnInit(): void {
    // @ts-ignore
    const id = +this.route.snapshot.paramMap.get('id');
    // @ts-ignore
    // this.album = (Albums.find((x) => x.id === id));
    this.getAlbum(id);
  }
  goBack(): void
  {
    this.location.back();
  }
  getAlbum(id: number): void
  {
    this.loading = true;
    // @ts-ignore
    this.albumsService.getAlbum(id).subscribe((album) => this.album = album);
    this.loading = false;
  }
  // tslint:disable-next-line:variable-name
  updateAlbum(): void
  {
    // console.log(this.album.title);
    this.album.title = this.updateTitle;
    // console.log(this.album.title);
    this.albumsService.updateAlbum(this.album).subscribe();
  }
}
